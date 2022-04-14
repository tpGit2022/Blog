Dagger2中常用的注解有
```
@Inject,@Named,@Qualifier,@Scope,@Singleton

@Component,@Subcomponent,@Lazy,@Module,@Provides,@Reusable
```

> 第一行的注解其实为`javax.inject`所有并非Dagger2的本身的注解，Dagger2依赖于`javax.inject`

`@Inject`和`@Module`用于提供依赖，`@Component`用于联系依赖和被依赖方。

**Dagger2根据返回值提供依赖**  
`@Inject`修饰字段代表该字段为依赖，需要外部注入，`@Inject`修饰构造方法为`@Inject`修饰的字段提供依赖实例，而`Module`则是为第三方库，无法用`@Inejct`修饰构造方法提供实例的类提供的解决方法，`@Module`用于修饰一个类，类中用`@Provides`修饰方法，代表提供某个实例。

> Dagger2文档中建议约定`@Module`修饰的类以`Module`结尾，类中`@Provides`修饰的方法以`provide`为前缀，

基于Dagger2以返回值来作为注入依赖的根据，下面来考虑几个问题：
1. 如果`@Provides`修饰的方法和`@Inject`修饰的构造方法返回类型一致，是否会报错，如果不，被注入的是那个依赖？简单来讲就是`@Provides`和`@Inject`那个优先级更高？
2. `@Provides`修饰的多个方法返回值相同，注入依赖是使用那个方法的返回值？同理如果`@Inject`注入了多个构造方法，当寻找依赖时该使用那个构造方法的返回值？

先放结论：对于情况1，`@Provides`优先级更高，情况2这需要借助`@Qualifier`注解或其子注解来解决限定。