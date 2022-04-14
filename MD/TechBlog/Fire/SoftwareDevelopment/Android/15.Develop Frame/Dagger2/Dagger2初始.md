> Dagger is a fully static, compile-time dependency injection framework for both Java and Android. It is an adaptation of an earlier version created by Square and now maintained by Google.
Dagger aims to address many of the development and performance issues that have plagued reflection-based solutions. More details can be found in this talk (slides) by +Gregory Kick.

> https://github.com/google/dagger

# 基础准备
依赖倒置原则
A.高层次的模块不应该依赖于低层次的模块，他们都应该依赖于抽象。
B.抽象不应该依赖于具体实现，具体实现应该依赖于抽象。

依赖注入是不在类中实例化其他依赖的类，而是先把依赖的类实例化了，然后以参数的方式传入构造函数中，
让上层模块和依赖进一步解耦。

**名词**  

1. 控制反转IoC(Inversion of Control)
    控制反转是面对对象编程的一种设计原则，用来降低代码间的耦合度，最常见方式是依赖注入，还有一种方式是依赖查找。通过依赖查找，对象在被创建的时候，有一个调度系统内的所有对象的外界实体，将其所依赖的对象的引用传递给它，也可以说依赖被注入到对象中。
2. 依赖注入DI(Dependency Injection)
3. 依赖查找DL(Dependency Lookup)

Dagger2 是Android中实现依赖注入的一种方式，而Dagger2是通过注解标记来注入依赖的。

**Dagger2 依赖`Javax.inject`,`Javax.inject`包含的注解如下**  
![20170602144258.png](../../../../../Pictures\20170602\20170602144258.png)  

| 注解符号 | 作用域 | 存在时期 |含义 |
|:---:|:---:|:--:|:--:|
| @Inject | METHOD, CONSTRUCTOR, FIELD | RUNTIME |
| @Named | 所有ElementType | RUNTIME |
| @Qualifier | ANNOTATION_TYPE |　RUNTIME |
| @Scope | ANNOTATION_TYPE | 　RUNTIME |
| @Singleton | 所有ElementType |　RUNTIME |

而 ***Provider*** 是一个接口，只定义了一个返回类型为泛型的get()无参方法。
**Dagger2自带的注解**  
![20170602144632.png](../../../../../Pictures\20170602\20170602144632.png)  

| 注解符号 | 作用域 | 存在期间 |　含义 |
|:--:|:--:|:--:|:--:|
| @Beta | 所有ElementType | SOURCE |
| @GwtIncompatible | 所有ElementType | CLASS |
| @Classkey | METHOD | RUNTIME |
| @ElementsIntoSet | METHOD | RUNTIME |
| @IntKey | METHOD | RUNTIME |
| @IntoMap | METHOD | RUNTIME |
| @LongKey | METHOD | RUNTIME |
| @Multibinds |  METHOD | RUNTIME |
| @StringKey | METHOD | RUNTIME |
| @CanReleaseReferences | ANNOTATION_TYPE | CLASS
| @ForReleasableReferences | FIELD, PARAMETER, METHOD |　RUNTIME
| @Binds |  METHOD | RUNTIME |
| @BindsInstance | METHOD | RUNTIME |
| @BindsOptionalOf | METHOD | CLASS |
| @Component | TYPE | RUNTIME |
| @MapKey | ANNOTATION_TYPE | RUNTIME |
| @Module | TYPE | RUNTIME |
| @Provides | METHOD | RUNTIME |
| @Reusable | 所有ElementType | RUNTIME |
| @Subcomponent | TYPE | RUNTIME |

# 基本注解符
## @Inject
## @Component
## @Module
## @Provides

# 参考资料
1. [依赖倒置原则](http://baike.baidu.com/item/%E4%BE%9D%E8%B5%96%E5%80%92%E7%BD%AE%E5%8E%9F%E5%88%99?fr=aladdin)
2. [控制反转](https://zh.wikipedia.org/wiki/%E6%8E%A7%E5%88%B6%E5%8F%8D%E8%BD%AC)
3. [依赖注解原理](http://codethink.me/2015/08/01/dependency-injection-theory/)
4. [Android Dagger2 学习笔记 (上) - 讲 Dagger 之前](http://zhaowen.io/post/dagger2/)
5. [维基百科Ioc](https://en.wikipedia.org/wiki/Inversion_of_control)
6. [维基百科Dependency Inject](https://en.wikipedia.org/wiki/Dependency_injection#Interface_injection_comparison)
7. [Android：dagger2让你爱不释手-基础依赖注入框架篇](http://www.jianshu.com/p/cd2c1c9f68d4)
8. [Android：dagger2让你爱不释手-重点概念讲解、融合篇](http://www.jianshu.com/p/1d42d2e6f4a5)
9. [Android：dagger2让你爱不释手-终结篇](http://www.jianshu.com/p/65737ac39c44)
10. [Dagger 2 完全解析（一），Dagger 2 的基本使用与原理](http://www.jianshu.com/p/26d9f99ea3bb)
11. [依赖注入神器：Dagger2详解系列](http://blog.csdn.net/weixin_36200883/article/details/52609866?locationNum=5)
12. [](http://blog.csdn.net/briblue/article/details/75578459?locationNum=7&fps=1)
13. [](http://www.cnblogs.com/mengdd/p/5613889.html?hmsr=toutiao.io&utm_medium=toutiao.io&utm_source=toutiao.io)
