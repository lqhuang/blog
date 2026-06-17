---
title: "Redesign Jotai AI's public API in a Jotai way"
created: 2025-09-30
updated: 2025-10-25
published: 2025-11-01
tags:
  - system-design
---

## Begin

The story starts since I hope to upgrade `jotai-ai` to fit the latest `ai-sdk` v5 architecture.

AI SDK[^gh:vercel/ai] is a poplular dev toolkit for building AI applications with rich features and integrations. The biggest advantage of using AI SDK is that it well maintained by Vercel and is iterating rapidly with also fast AI technology advancements. The biggest problem is the same that it's evolving quickly [^ai-sdk-6-beta], given great maintenance efforts to the downstream libraries (like `jotai-ai`).

Of course, things should evolve. The released AI SDK 5 introduces a fresh new architecture and a lot of improvements over the previous "chaos", which the major benefit of new architecture is to make the SDK more modular and extensible with external tools/storage.

It's great news for `jotai-ai` because we can now leverage the new architecture to help the API stable and extensible to reduce the maintenance burden. So I open a Pull Request to upgrade `jotai-ai` to AI SDK 5. Bascially, this post is a relection and summary of myself in this PR [jotaijs/jotai-ai #20](https://github.com/jotaijs/jotai-ai/pull/20) with better linearity.

[^gh:vercel/ai]: [vercel/ai](https://github.com/vercel/ai): The AI Toolkit for TypeScript. From the creators of Next.js, the AI SDK is a free open-source library for building AI-powered applications and agents <https://ai-sdk.dev>

[^ai-sdk-5]: [AI SDK 5 | Vercel](https://vercel.com/blog/ai-sdk-5)

[^ai-sdk-6]: [Announcing AI SDK 6 Beta | AI SDK](https://v6.ai-sdk.dev/docs/announcing-ai-sdk-6-beta)

## Before "current instant" and background

I'm Jotai user while not a core contributor. I have used Jotai in several projects and libraries, including `jotai-ai`. I really like Jotai's primitive and flexible design, which makes state management more enjoyable and seamless with React.

I'm a FP lover, though I advocate sensible pragmatism, not like a purist like FP everywhere . Find it right path and make things work well is more important for me.

Then while I'm playing with AI toys, I still use jotai to manage state in my projects. I used my custom jotai atoms to manage chat messages, status, and errors, until I found [jotaijs/jotai-ai](https://github.com/jotaijs/jotai-ai) created by [@gh:himself65](https://github.com/himself65). `jotai-ai` is still a PoC project, but it's enough for me to try and build some simple AI chat applications quickly.

In the first few versions, @gh:himself65 implemented `jotai-ai` by wrapping the upstream `useChat` hook from `@ai-sdk/react`.

```ts
import { useAtomValue, useAtom, useSetAtom } from 'jotai'
import { chatAtoms } from 'jotai-ai'

const { messagesAtom, inputAtom, submitAtom, isLoadingAtom } = chatAtoms()

function Messages() {
  const messages = useAtomValue(messagesAtom)
  return (
    <>
      {messages.length > 0
        ? messages.map((m) => (
            <div key={m.id} className="whitespace-pre-wrap">
              {m.role === 'user' ? 'User: ' : 'AI: '}
              {m.content}
            </div>
          ))
        : null}
    </>
  )
}

function ChatInput() {
  const [input, handleInputChange] = useAtom(inputAtom)
  const handleSubmit = useSetAtom(submitAtom)
  return (
    <form onSubmit={handleSubmit}>
      <input
        value={input}
        placeholder="Say something..."
        onChange={handleInputChange}
      />
    </form>
  )
}

function App() {
  const isLoading = useAtomValue(isLoadingAtom)
  return (
    <main>
      <Messages />
      <ChatInput />
      {isLoading ? <div>Loading...</div> : null}
    </main>
  )
}
```

And by the project. @gh:himself65 also introduce a new `jotai-lazy` to help lazy load initial state from server side or whatever async sources.

Here are serveral problems. That, my pre existed logic may not work well with `jotai-ai` because:

- `jotai-ai` use it self messagesAtom to manage chat messages state internally, which means I cannot customize or derive messages from other atoms easily.
- I cannot initialize messages from server side easily, since `jotai-ai` always initialize messagesAtom as an empty array internally.

So, I open an issue [jotaijs/jotai-ai #15](https://github.com/jotaijs/jotai-ai/pull/15) to discuss how to improve `jotai-ai` to fit more use cases and scenarios.

Propose some ideas and discuss with @gh:himself65, finally I decide to upgrade `jotai-ai` to fit the latest AI SDK v5 architecture and redesign the public API of `jotai-ai` in a more "Jotai way".

```ts
const {
  // basic abstractions
  inputAtom,
  messagesAtom,
  streamDataAtom,

  // status flag containers,
  isLoadingAtom,
  errorAtom,
  statusAtom,

  // actions
  stopAtom,
  appendAtom,
  reloadAtom,
  addToolResultAtom,
  resumeAtom,
  resetAtom,

  // configurable handlers
  onErrorAtom,
  onResponseAtom,
  onToolCallAtom,
  onFinishAtom,

  // configurable options
  streamProtocolAtom,
  keepLastMessageonErrorAtom,
  maxStepsAtom,
  sendExtraMessageFieldsAtom,
  bodyAtom,
  headersAtom,
  credentialsAtom,
  prepareRequestBodyAtom,
} = makeChatAtoms({ chatIdAtom, initialMessagesAtom, initialInputAtom })
```

1. Split main user interface to two functions `makeChatAtoms` and `useChat`. Let `useChat` expose useful and similar handlers/states like upstream `useChat` (`ai/react`), and left `makeChatAtoms` contains low level atoms for advanced users. Indeed, `makeChatAtoms` only controls how client interactive with remote stream data (append and receive new messages), and left all others into `useChat` in order that advanced users could implement theirs `inputAtoms`, `sumbitAtoms`. Built-in `useChat` could be just an official reference implementation has the same features with upstream projects.

2. Accept a user defined `messagesAtom` from outside. Like

   ```ts
   const messagesAtom = atom<Message[]>([])

   const {
     // state data containers,
     isLoadingAtom,
     errorAtom,
     dataAtom,

     // actions
     stopAtom,
     appendAtom,
     reloadAtom,

     // handlers
     onErrorAtom,
     onResponseAtom,
     onToolCallAtom,
     onFinishAtom,
   } = makeChatAtoms({ messagesAtom })
   ```

   In this way, users could decide how to prepare their UI messages, whatever derived from other states or initialed from fetch or even SSR.

   ```ts
   // Initial messages in SSR approach
   // so `makeChatAtoms` doesn't need to consider
   // how to deal with initial messages or initial input.
   import { useHydrateAtoms } from 'jotai/utils';

   const messagesAtom = atom<Message[]>([]);

   const Component = ({ initChatMesssages }:{ initChatMesssages: Message[] }) => {
     useHydrateAtoms([[messagesAtom, initChatMesssages]])

     const messages = useAtomValue(messagesAtom)

     return <Chat>{messages}<Chat/>
   }
   ```

3. It would be easier to introduce more features and keep flexibility by using this architecture. We're able to add more states like `firstTokenReceived` or action like `deleteAtom` in the future without breaking up signatures of `useChat`.

Also, there are several issues I haven't confirmed and figured out clearly:

1. In current implements, all deprecated API and parameters are literally deprecated. And the `ai` project has already released alpha candidates of the next `v4` version.

2. Current callback handler like `onErrorAtom`, ..., `onResponseAtom` is initialed by `makeChatAtoms` and cloud be updated by `useChat`. I'm not sure whether it's a correct design or proper usage of atoms. For now, it's just implemented to fit upstream UI test cases easily.

3. I hope we could add a generic type interface for `Body` into `makeChatAtoms`. This data type can be shared between server endpoint and user client. It's more safe and ergonomic to make sure correct data being sent and parsed.

## What I first do

```ts
/**
 * Declare jotai atoms and jotai chat state
 */
import { JotaiChat, JotaiChatState } from 'jotai-ai/v5/chat'

// Custom yourself `ChatMsg` by extending `UIMessage`
export const messagesAtom = atom<ChatMsg[]>([])
export const statusAtom = atom<ChatStatus>('ready')
export const errorAtom = atom<Error | undefined>(undefined)

export const chatState = new JotaiChatState<ChatMsg>({
  messagesAtom,
  statusAtom,
  errorAtom,
})
export const jotaiChat = new JotaiChat<ChatMsg>({
  id: 'chat-id-xxxxx',
  transport: new DefaultChatTransport({
    api: CHAT_API_ENDPOINT,
  }),
  state: chatState,
  onError: (error) => {
    if (error) {
      toast({ type: 'error', description: error.message })
    }
  },
})
```

```ts
/**
 * Use `jotaiChat` in components
 */
import { useChat } from '@ai-sdk/react';
import { jotaiChat } from './store.ts'

export const ChatComponent = () => {

  const chatHelpers = useChat<ChatMsg>({
    chat: jotaiChat,
    experimental_throttle: 100,
  });

  const { messages, status, sendMessage, stop } = chatHelpers;

  return (<>
    ...
    ...
  <>)
}
```

## Where I fail

## The Aha moment

Thank @songkeys for his innovated solutions. I tried it, and it actually works in some test cases, I'm also grad to learn something new from it! Unfortunately, that's not enough.

```ts
export function useJotaiChat({ chat: Chat, ...opts }) {
  const [messages, setMessages] = useAtom(messageAtom)
  const [status, setStatus] = useAtom(statusAtom)
  const [error, setError] = useAtom(errorAtom)

  useEffect(() => {
    const unregisterMessagesCallback = chat['~registerMessagesCallback'](() => {
      setMessages(chat.messages)
    }, 50)

    const unregisterStatusCallback = chat['~registerStatusCallback'](() => {
      setStatus(chat.status)
    })

    const unregisterErrorCallback = chat['~registerErrorCallback'](() => {
      setError(chat.error)
    })

    return () => {
      unregisterMessagesCallback()
      unregisterStatusCallback()
      unregisterErrorCallback()
    }
  }, [chat, setMessages, setStatus, setError])

  const ret = useChat({
    chat,
    ...opts,
  })

  return {
    ...ret,
    messages,
    status,
    error,
  }
}
```

Then say hello to all subscribers, I'm here to sharing my progress recently.

My first try was structurally inspired (emmmm, almost copied) from [FranciscoMoretti's Gist - Zustand + AI SDK useChat Integration](https://gist.github.com/FranciscoMoretti/5e723bde74420e1b79e545da40ba8d0f). However, it just "looks great". When I added unit tests, my first version failed everywhere (for example, infinite re-render loops). Then I started to debug and dive into the internal details of `useChat` from `@ai-sdk/react`. And I also tried to optimize via `useMemo` or `useCallback` approach to avoid infinite loops, through they may not work at all.

The new `useChat` hooks in new v5 architecture is simpler than before, which only has some codes to let `useSyncExternalStore` and `AbstractChat`(w/ `ChatTransport`) work together.

I was thinking, the key of the solution is how to cooperate `jotai` and `useSyncExternalStore` (I'm not very sure does #11 also result in similar cases). Finally, during my research work, I found Dashi's great articles to solve my confuses! I strongly recommend who're interested in this PR to read [When I Use Valtio and When I Use Jotai](https://blog.axlight.com/posts/when-i-use-valtio-and-when-i-use-jotai/) and optional [Why `useSyncExternalStore` Is Not Used in Jotai ](https://blog.axlight.com/posts/why-use-sync-external-store-is-not-used-in-jotai/).

I repost the most enlightening illumination here

![tech-diff](https://pbs.twimg.com/media/EysxETLVoAEKtkc?format=jpg&name=4096x4096)

TL;DR:

1. `zustand` or `valtio` are naturally cooperated much better with `useExternalSync` since that's why they are created.
2. A **bridge** is inevitably required between `jotai` and external state.

Hence, my original schedules would be:

1. Introduce `zustand`/`valtio` as adapter middleware
   - Pros: there are very matured `jotai-zustand`/`jotai-valtio` packages.
   - Cons: It's a wired "Frankenstein" solution, and user probably have its own zustand dep version.
2. Implement a simple `jotai-swr` (like `jotai-tanstack-query`) to bridge them.
   - Pros: Since `ai` package has also delivered `swr` package, it's a very friendly solution. What's more, we can improve and get an individual `jotai-swr` in the future.
   - Cons: May not the optimal solution. And need more implementations and tests to ensure things work well.
   - Extra bonus: In `useChat` hooks, `swr` is used in default chat transport implicitly, where the "implicit" means you could customize yourself transport without `swr`. But in `useCompletion` and `useObject`, these two hooks are more stateless compare to `useChat`, `swr` is a built-in and enforced dependency. If we have `jotai-swr`, it would be easy to migrate `useCompletion` and `useObject` to `jotai-ai`.
3. Maintain internal jotai chat state with `atomWithObserver`
   - Pros: Most "jotai native" and primitive solution. Probably will minimize extra re-renders while cooperating.
   - Cons: Browser native `Observable` still in TC39 Stage 2 or 3? Only Chrome after 135 version implement it as I know now. End developers will be required to add a polyfill package, or else introduce `rxjs`.

PS: I'm now trying to play some magical/dark tricks via jotai `store` with subscription methods as attempts.

Now, let me clarify why @songkeys' approach is not enough:

1. The approach is very similar to my previous PR to fix v4 adaptions (#16) which may cause one extra re-render. (Or maybe not, honestly, I'm not sure.)
2. That's not "jotai style". What's the "jotai style"? My understanding and explanation here is decomposing state management and react component in a most optimal approach. There are two points:
   - `useJotaiChat` wouldn't use again in child component, you need to pass the handler to children as props.
   - Both `useAtom` and `useJotaiChat` will expose `setMessages` handler, and they have different **behaviors**. That's not a safe pattern in API design.

But I indeed get inspired from @songkeys' suggestions. Especially, I have new ideas and new directions when I'm writing and organizing this reply (aha, that's how discussions work 🤣).

My eventual desired goals of `jotai-ai`:

1. Collaborate with other atoms natively
   - We could also represent it to work seamlessly with other packages in Jotai's ecosystem.
2. Reduce re-renders as more as possible.
3. Follow upstream changes with minimal efforts.

So the API will be like:

```ts
const initialMessagesAtom = atom(...);
const initialChatId = atom(...);

// Just to show the most jotai primitive function call
// const { messagesAtom, statusAtom, errorAtom } = atomAIChat(
//   get => {},
//   (get, set, ...) => {},
// );
const { messagesAtom, statusAtom, errorAtom } = atomWithAIChat({
  initialMessagesAtom
});
// So what the `jotai-ai` really do is to help end developers to write getter and setter.
// Keep the dark detail inside of `atomWithAIChat`
// and let end users to compose or derive atoms as they hope!.

const ChatComponent = () => {
  const [messages, setMessages] = useAtom(messagesAtom)
  // Or actually we could customize a hook to expose more handlers
  const {messages, sendMessages, resendMessages, abortSendingMessages} = useChatMessagesAtom(messagesAtom)


  return (<>
    ...
    ...
  <>)
}
```

IMHO, that's the "Jotai style", that's also my motivation of PR #15 which I look like to forget yet.

What I have mistaken is I hope to reuse `useChat` and implement `AbstractChat` into `JotaiChat`, but @songkeys let me aware that I should reuse `DefaultChatTransport`, and reimplement both `useChat` and `AbstractChat`. What's more, the brilliant point is the `AbstractChat` could be also featured as an adapter to let user bridge other state management into `jotai-ai`, which means user can choose to pass `initialMessageAtoms` into `atomWithAIChat` or pass `ZustandChat` into `useJotaiChat`.

## What comes when you embrace entirely the Jotai philosophy

After discussion with @songkeys, I have updated the design of API. Adding one atom constructor `atomWithChat` and one hook function `useChatAtomValue`. Basically, try to reuse `AbstractChat` and rewrite `useChat` to match the philosophy of Jotai itself.

First, declare the `chatAtom`

```ts
import { Chat } from '@ai-sdk/react'

const { chatAtom } = atomWithChat((get) => {
  return new Chat<UIMessage>({
    // Put `useChat`'s `ChatInit` arguments here.
  })
})
```

then, we could use the `chatAtom` in the component like other atoms with customized hook `useChatAtomValue`

```ts
const Component = () => {
  const {
    messages,
    sendMessage,
    error,
    status,
    id, // the same return of `useChat` hook
  } = useChatAtomValue(chatAtom);

  ...

  return (<>
    ...
  </>)
}
```

Yes, the API is very similar to the `jotai-tanstack-query`, the limitation parts we will discuss later.

For the first input argument of the `atomWithChat`, it's just a reader function, so we could compose other atoms and state easily,

```ts
import { useHydrateAtoms } from 'jotai/utils'

const idAtom = atom<string>('initial-id')
const messagesAtom = atom<UIMessage[]>([])
const { chatAtom } = atomWithChat((get) => {
  return new Chat({
    id: get(idAtom),
    messages: get(messagesAtom),
  })
})

const Component = ({ id: idParam }: { id: string }) => {
  useHydrateAtoms([[idAtom, idParam]])

  const [idKey, setId] = useAtom(idAtom)
  const { messages, sendMessage, error, status, id } =
    useChatAtomValue(chatAtom)

  if (idKey != id)
    throw new UnreachableError("they're definitely identical in value")

  return <>...</>
}
```

Compatible with SSR and whatever other approaches to initial ID or messages by Jotai style atoms (like `atomFamily`).

That's all! No more dark magic, just Jotai.

Current results of UI tests (adapt `useChat` test cases from upstream) are added as follows:

This time, I have passed almost all UI tests, except one corner case, which may fix later.

### But it's not perfect yet with limitations

**`useChatAtomValue` is forcedly required now.**

Unlike `jotai-tanstack-query`, we cannot use native jotai hooks like `useAtom`/`useAtomValue` (`useSetAtom` is fine).

```ts
const { messages, status, sendMessage } = useAtomValue(chatAtom)
const { messages, status, sendMessage } = useChatAtomValue(chatAtom)
```

⚠️ Unfortunately, The above two hooks **have different behaviors** now. The good news is the caused reason is clear and fixable. In general, we have no `atomWithExternalSync` or `atomWithObservable`, so we cannot subscribe change events from external sources inside `atomWithChat`. Hence, we have to implement the sync effect inside `useChatAtomValue` or `useChatAtom`, see the following example:

```ts
// Yeah, I try to expose extra atoms as small helpers.
const { idAtom, errorAtom, statusAtom, messagesAtom, chatAtom } = atomWithChat(
  () => new Chat({}),
)

// But we can't just
const [status, setStatus] = useAtom(statusAtom)
// `status` won't change anymore if we execute `setStatus('...')`, since it never syncs to external store after creat.

// The current solution is implementing a `useStatusAtom` (pseudo, just for explaining)
import { useSyncExternalStore } from 'react'

export function useStatusAtom(chatAtom) {
  const chat = useAtomValue(chatAtom)
  const { setStatus } = useSetAtom(chatAtom)

  const status = useSyncExternalStore(
    chat['~registerStatusCallback'],
    () => chat.status,
    () => chat.status,
  )

  return [status, setStatus]
}
```

That's why they have different behaviors now. If we can move the sync effect logic into `atomWithChat` via `atomWithExternalStorage`, then we unify them in the future.

1. [Synchronizing atoms with external sources pmndrs/jotai#1487](https://github.com/pmndrs/jotai/discussions/1487)
2. [Recoil Sync Atom Effect - syncEffect()](https://recoiljs.org/docs/recoil-sync/sync-effect)

Current solution: We can try to add **explicit warnings** in docs to tell users to avoid mistakes.

**I don't implement `setMessages` (handler in `useChat` returns) yet.**

As ai-sdk [doc](https://ai-sdk.dev/docs/reference/ai-sdk-ui/use-chat#set-messages) say:

> `setMessages`: Function to update the messages state locally without triggering an API call. Useful for optimistic updates.

But actually, IMHO, it's quite unusable or unsafe operation. There is no more mechanism to deal with what if optimistic updates failed even use the official API. The user still need to implement all other details. So I think we should left this part to the user self, if they know what they're doing, `setMessages` is not difficult to implement with `jotai-ai`

## Contribute `atomWithExternalStorage` to Jotai

Oct 25, 2025

@gh:himself65 is too busy recently.

I start to think could I just ask jotai upstream for help or just implement a downgraded version of `atomWithExternalStorage` for jotai. 🤔
