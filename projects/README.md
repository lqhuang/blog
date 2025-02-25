After resigning from my last position in December 2024, I have had a lot of ideas and projects emerge in my mind, based on my experiences and observations from the past years.

Some of these ideas are just for fun, some are for personal hobbies, and some are niche ideas. Some of them may even be wrong. Nevertheless, I just write them down, try to build them in private or public (depending on the type of project) and share the progress with the community, while also considering my next significant career move.

They’re not mature, they’re too young, or they’re even just impossible concepts based on my incorrect understanding. Just ignore them, contribute to them, sponsor them, or even discuss them, including pointing out my mistakes. I’m open to any feedback, suggestions, and collaboration.

<!-- I will dedicate myself to these ideas until they’re done, they grow to maturity, or they’re not fun anymore, or they turn out to be totally wrong. Then I can move on to the next idea. -->

## xattrs and rekki

**Motivation**

Starting with the 3.13 release, CPython has experimental support for a build of Python called free threading where the global interpreter lock (GIL) is disabled. Free-threaded execution allows for full utilization of the available processing power by running threads in parallel on available CPU cores.

The whole numerical computing and AI community will benefit from this new feature. This advancement, however, comes with challenges. It’s necessary to verify its compatibility in production environments. Therefore, I hope to build some tools and libraries to support the free-threading model in Python.

- `xattrs` is eXtensible toolkits of your attrs and dataclasses types with sensible default behaviors.
  - leverage the power of JAX `PyTree` idea to serialize and deserialize the structured data
- `rekki` is an experimental reactive programming framework for Python. Utilizing the free-threading model, it will provide a new way to build asyncio services and applications.

Progress:

- [x] [lqhuang/xattrs](https://github.com/lqhuang/xattrs): An eXtensible serializing and deserializing toolkit for Python strucuted classes (eg: dataclasses, attrs)
  - Completed PoC and MVP
  - Currently polishing the code and documentation
- [ ] [rekki-dev/rekki](https://github.com/rekki-dev/rekki)
  - successor of `mode-ng` with free-threading support
  - [lqhuang/mode-ng](https://github.com/lqhuang/mode-ng): mode asyncio services framework (next-generation)
- [ ] andata: lock-free ringbuffer for free-threading concurrency model in Python

**Potential sustainable model**

- Open source sponsorship
- Community-driven development
- Commercial support

I hope it could become as awesome as the Pallets community <https://palletsprojects.com/>.

## CHMK AI

> previous chaos-monkey.ai <https://chaos-monkey.ai/>

A practical AI platform

- For users: A **collaborative** AI teamspace to help them work together with cutting-edge AI technologies. Think of it as Figma for scientists and developers.
- For developers: A **headless** AI observability platform to build, ship, and monitor agentive systems. Headless observability combines two core concepts: headless architecture and the decoupled observability stack. Storage, ingestion, and visualization are decoupled, resulting in greater flexibility and lower costs.

It’s a SaaS model and a proprietary project. Yes, I need to make money to support my family.

Progress

- Finished the MVP
- Waiting to launch

## Scala Native and DAX

**What is DAX?**

DAX is

- A programming DSL in Scala Native with JAX & OpenXLA for machine learning and scientific computing
- State-of-the-art Dependent Type System for type-level numerical computing
- Designed for high performance and productivity to accelerate machine learning tasks

**Motivation**

JAX, the new framework designed to address the perceived shortcomings of TensorFlow 2.0, is strongly attracting my interest and that of others. (For more information, check out [JAX - Why is Everyone So Excited About This Framework](https://yash-sri.xyz/blog/jax_blog)).

<!-- At least for undergrudate students in Physics, a numpy interface and stable `scipy.integrate.solve_ivp`, `scipy.integrate.slove_bvp` are enough for most of the cases they will encounter in their college life. -->

Unfortuanelly, The commbined PyTorch x CUDA solutions has dominated the industry for years. But the more and more use cases and mature production ready model from JAX/Flax, and some good news from the JAX team / Google DeepMind let me feel hopes again. For example, unlike pytorch is domnated to Linux Foundation, the jax repo has moved out from the google organization to the [jax-ml organization](https://github.com/jax-ml) recently. It's a good sign that the project is more and more community driven.

Unfortunately, the combined PyTorch and CUDA solutions have dominated the industry for years. However, the increasing number of use cases and mature production-ready models from JAX/Flax, along with some good news from the JAX team and Google DeepMind, have given me hope again. For example, unlike PyTorch, which is donated to the Linux Foundation, the JAX repository has recently moved out of the Google organization to the [jax-ml organization](https://github.com/jax-ml). This is a good sign that the project is becoming more impartial and not solely driven by Google.

Nowdays, the ML/AI ecosystem in Python, such as PyTorch and JAX, is exploring how to apply Dependent Type theory to numerical computation frameworks. Given my adaption for Scala and functional programming, I thought, why not try Scala? Dotty features the most advanced compiler and type systems. If one were to choose the most suitable language right now that resembles Python but has a richer ecosystem and more excellent language design, Scala 3 would be the best and only choice.

The main problem of this idea is that the developement of related projects is purely drivend by industry and giants.

**Open questions**

The project Swift for TensorFlow, initiated in the earliest days, featured a discussion on why Swift was chosen, which is available at https://github.com/tensorflow/swift/blob/main/docs/WhySwiftForTensorFlow.md. Despite its retirement, the project has left behind many valuable insights. Fast forward to 2023, Chris Lattner led the release of Mojo, reinforcing the continued appeal and value of improved languages for machine learning/AI in the industry. Notably, Chris Lattner, one of Swift’s founders, was also a leader in the Swift for TensorFlow project.

In 2018, when Swift4TF was selecting its programming language, the reasons Scala was deemed unsuitable have ceased to exist, thanks to Scala’s evolution and the official release of Dotty. Particularly, the development of Scala Native has expanded Scala’s possibilities significantly.

However, there are still many challenges:

- Essential tooling is missing (like Bazel support for Scala Native) or requires significant improvements
- The ecosystem is not as mature as Python’s
- It’s challenging to find a good business model for the project. It’s definitely a "war" with giants in the industry. They contribute substantial resources to develop and verify current tools. If the progress is not good enough and not widely adopted, it’s hard to survive.

It definitely won’t survive long as a for-fun project. It’s a serious endeavor that requires significant resources and efforts.

The best outcomes would be to become part of some non-profit foundations sponsored by industry giants, or even to raise VC funding.

**Progress**

In the first few years, I would try to implement a common interpolation layer for Scala Native and JAX. Besides, I contributed to Scala 3 and SN projects to improve their eco systems.

- [x] [com-lihaoyi/requests-scala - chore: Upgrade build deps to ensure compatible with Scala Native #178](https://github.com/com-lihaoyi/requests-scala/pull/178)
- [ ] [scala-native/scala-native - Support for \`java.net.http.HttpClient\` #4104](https://github.com/scala-native/scala-native/issues/4104)
  - Status: Onging
  - [lqhuang/scala-native-http](https://github.com/lqhuang/scala-native-http): A proof of concept project to implement `java.net.http` module since Java 11 for Scala Native
- [ ] [lqhuang/curtus](https://github.com/lqhuang/curtus): Scala Native bindings for Python -- Python Curtus (aka: Blood Python)
  - Status: WIP

<!-- - [lqhuang/dax](https://github.com/lqhuang/dax): No description, website, or topics provided. -->

## Single threading is doing good.

Severless is everywhere now. Which means the single threading is doing good.

I have some ideas to build an universal runtime based on `libuv` to brige different languages (Python, JavaScript, Rust, Zig, ..., etc) and runtime into one event loop per thread. Embrace the Thread-per-Core (TPC) model to make the best use of the modern CPU architecture.

... Still brainstorming.

<!-- ## Templates

- Motivation
- Design
- Status
- Implementation
- Evaluation
- -->
