[TOC]

# 前言

# 仓库

# 依赖
## 配置
## 依赖冲突

Gradle 依赖相关的内容的官方文档链接 https://docs.gradle.org/current/userguide/introduction_dependency_management.html



先来看一段熟悉的依赖管理代码


```
dependencies {
    
    ....
    implementation fileTree(dir: 'libs', include: ['*.jar'])
    androidTestImplementation('com.android.support.test.espresso:espresso-core:2.2.2', {
        exclude group: 'com.android.support', module: 'support-annotations'
    })
    api 'com.android.support:appcompat-v7:25.3.0'
    compile 'com.android.support.constraint:constraint-layout:1.0.2'
    testImplementation 'junit:junit:4.12'
    implementation 'com.jakewharton:butterknife:8.6.0'
    annotationProcessor 'com.jakewharton:butterknife-compiler:8.6.0'
    ...

}
```

依赖库的管理是通过接口 `DependencyHandler`, 位于 `org.gradle.api.artifacts.dsl`  
https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/dsl/DependencyHandler.html


https://docs.gradle.org/current/javadoc/org/gradle/api/plugins/JavaPlugin.html


通过Grovvy脚本修改版本号解决冲突
在其存在冲突的module中的build.gradle文件中加入下面代码，原理就是通过遍历所有依赖，并修改指定库的版本号

其中

```
configurations.all {
    resolutionStrategy.eachDependency { DependencyResolveDetails details ->
        def requested = details.requested
        if (requested.group == 'com.android.support') {
            if (!requested.name.startsWith("multidex")) {
                details.useVersion '28.0.0'
            }
        }
    }
}
```

然后rebuild一下即可

# 依赖配置

* 

# 依赖冲突

有了上面的基础，应该会容易理解。dependencies是会被delegate给DependencyHandler，不过如果你到DependencyHandler中去查找，会发现找不到上面的implementation、testImplementation等方法。那它们有到底是怎么来的呢？亦或者如果我们添加了dev flavor，那么我又可以使用devImplementation。这里就涉及到了groovy的methodMissing方法。它能够在runtime(*)中捕获到没有定义的方法。

至于(*)是gradle的methodMissing中的一个抽象感念，它申明在MethodMixIn中。

对于DependencyHandler的实现规则是：
在DependencyHandler中如果我们回调了一个没有定义的方法，且它有相应的参数；同时它的方法名在configuration(*)中；那么将会根据方法名与参数类型来调用doAdd的相应方法。

对于configuration(*)，每一个plugin都有他们自己的配置，例如java插件定义了compile、compileClassPath、testCompile等。而对于Android插件在这基础上还会定义annotationProcessor，(variant)Implementation、(variant)TestImplementation等。对于variant则是基于你设置的buildTypes与flavors。

另一方面，由于doAdd()是私用的方法，但add()是公用的方法，所以在dependencies中我们可以直接使用add

dependencies {
    add('implementation', 'io.reactivex.rxjava2:rxjava:2.0.4')
    add('testImplementation', 'junit:junit:4.12')
    add('annotationProcessor', 'org.parceler:parceler:1.1.6')
}
注意，这种写法并不推荐，这里只是为了更好的理解它的原理。

# 参考资料
1. [Gradle-API-Interface DependencyHandler](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/dsl/DependencyHandler.html)
2. [android gradle依赖：implementation 和compile的区别](https://blog.csdn.net/qijingwang/article/details/79805794)
3. [com.android.support版本冲突的解决办法](https://blog.csdn.net/yuzhiqiang_1993/article/details/78214812)
4. [Android Gradle系列-原理篇](https://segmentfault.com/a/1190000019211742)
5. [Gradle-API-JavaPlugin](https://docs.gradle.org/current/javadoc/org/gradle/api/plugins/JavaPlugin.html)
6. [The Java Plugin](https://docs.gradle.org/current/userguide/java_plugin.html)
7. [Managing Dependency Configurations](https://docs.gradle.org/current/userguide/managing_dependency_configurations.html)
8. [Introduction to Dependency Management](https://docs.gradle.org/current/userguide/introduction_dependency_management.html)