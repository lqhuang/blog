# Design Patterns

## Six Rules

SOLID

1. 单一职责原则 (*S*ingle Responsibility Principle)
2. 开闭原则 (*O*pen Close Principle)
3. 里氏替换原则 (*L*iskov Substitution Principle)
4. 接口隔离原则 (*I*nterface Segregation Principle)
5. 依赖倒置原则 (*D*ependence Inversion Principle)
6. 迪米特法则 (Law Of Demeter)
7. 合成复用原则 (Composite Reuse Principle, CRP)

ref: (https://blog.csdn.net/zhengzhb/column/info/pattern/1)

## 23-Design-Patterns

创建型模式(Creational Pattern)对类的实例化过程进行了抽象，能够将软件模块中对象的创建和对象的使用分离。为了使软件的结构更加清晰，外界对于这些对象只需要知道它们共同的接口，而不清楚其具体的实现细节，使整个系统的设计更加符合单一职责原则。

- 简单工厂模式(Simple Factory)
- 工厂方法模式(Factory Method)
- 抽象工厂模式(Abstract Factory)
- 建造者模式(Builder)
- 原型模式(Prototype)
- 单例模式(Singleton)

结构型模式(Structural Pattern)描述如何将类或者对 象结合在一起形成更大的结构，就像搭积木，可以通过 简单积木的组合形成复杂的、功能更为强大的结构。

- 适配器模式(Adapter)
- 桥接模式(Bridge)
- 组合模式(Composite)
- 装饰模式(Decorator)
- 外观模式(Facade)
- 享元模式(Flyweight)
- 代理模式(Proxy)

行为型模式(Behavioral Pattern)是对在不同的对象之间划分责任和算法的抽象化。

- 职责链模式(Chain of Responsibility)
- 命令模式(Command)
- 解释器模式(Interpreter)
- 迭代器模式(Iterator)
- 中介者模式(Mediator)
- 备忘录模式(Memento)
- 观察者模式(Observer)
- 状态模式(State)
- 策略模式(Strategy)
- 模板方法模式(Template Method)
- 访问者模式(Visitor)
