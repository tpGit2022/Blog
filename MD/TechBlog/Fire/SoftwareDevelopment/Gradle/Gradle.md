[TOC]  

> update 2019.10.01

Gradle 是一款专注灵活和性能的开源的全自动构建工具，Gradle 脚本采用 Groovy 或者 Kotlin 语言编写。

不得不吐槽一下苦逼的 Android 开发，编写代码用 Java，Kotlin，写构建脚本又要切到 Groovy。在三种语言中切来切去的 Android 开发真的太难了，所幸 Gradle 开始支持 Kotlin 想象不久的将来 Kotlin 将一统 Android 天下，Android Studio 新建项目的将会默认使用 `build.gradle.kts` 作为构建脚本。


gradle  和 gradlw-wrapper

gradle 用于构建的工具
gradlew-wrapper 对 gradle的一层封装保证在在没有gradle环境下也可正常编译项目。

build.gradle 一个项目至少存在两份build.gradle。应用模块和库模块均有一份build.gradle，整个project也会有一份build.gradle。
settings.gradle 指明当前project所引用的应用模块和库模块。

模块内build.gradle可以重写根目录下面的gradle，模块内的
```
defaultConfig{
    applicationId    
}
```

管理依赖
远程仓库(repositories)
依赖(dependencies)

依赖需要定义三个元素 group，name，version
```
dependencies {
    compile 'com.google.code.gson:gson:2.3'
    compile 'com.squareup.retrofit:retrofit:1.9.0'
    compile  fileTree(dir:'libs',include['*.jar'])
}
```


Gradle Task

```
task task_name_1(type : Copy) {
    ....   
}
```

  task_name_1 是Copy的子类，type表示task_name_1是Copy类型的Task


Gradle Wrapper 是对 Gradle 的包装，简而言之 Gradle Wrapper 可以让 Gradle 项目在未配置 Gradle 的环境下依旧正常运行， Gradle Wrapper 会先下载相关的 Gradle 的版本，然后执行任务，这在团队合作中保持相同环境很有用。

执行 `gradle wrapper` 即可完成封装

```
│  .gitignore
│  build.gradle.kts
│  gradlew
│  gradlew.bat
│  settings.gradle.kts
│
└─gradle
    └─wrapper
            gradle-wrapper.jar
            gradle-wrapper.properties
```

`gradlew` 用于 Linux/MacOS。`gradlew.bat` 用于 Windows。

`gradle/wrapper/gradle-wrapper.properties` 的内容如下：

```
distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
distributionUrl=https\://services.gradle.org/distributions/gradle-5.6.2-bin.zip
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists
```

distributionBase 的取值只能是 GRADLE_USER_HOME 和 Project。


针对 Gradle 脚本中的配置，如何直到那些配置的名称，答案是看源码，事实上Gradle的官方文档不尽如人意，常用配置文档上也是语焉不详。因而查看源码才是最终解决之道，在 `build.gradle` 中一般是直接通过 ctrl+左键 跳转到源码当中去，但有时候也存在无法跳转的情况下先说明一下源码的情况

事实上 Android 开发中 build.gradle 会利用到两部分的源码 gradle和gradle-android-plugin 也就是 gradle/wrapper/gradle-wrapper.properties 和 项目的build.gradle中 

```
dependencies {classpath 'com.android.tools.build:gradle:3.5.0'}
```

和 android 相关的配置是需要在 android-plugin 中找的，譬如上图就需要在 com.android.tools.build/xxx/gradle-3.5.0-sources 中寻找

譬如打包多个版本中常用到一段 build.gradle 的脚本如下:

```
    android.applicationVariants.all { variant ->
        variant.outputs.all {
            if (buildType.name == 'release') {
                variant.getPackageApplicationProvider().get().outputDirectory = new File(project.rootDir.absolutePath + "/app/release/")
//                variant.getPackageApplication().outputDirectory =
                outputFileName = "xxx-v${variant.versionName}-${releaseTime()}.apk".trim()
            } else if (buildType.name == 'debug') {
                outputFileName = "xxx-debug-v${variant.versionName}-${releaseTime()}.apk".trim()
            } else {
                outputFileName = "xxx-v${variant.versionName}-${releaseTime()}.apk".trim()
            }
        }
    }
```

直接 ctrl+左键 点击 android.applicationVariants 可能无法跳转到对应的源码中，这时如果需要得知可用的配置，就需要去查看源码，


https://blog.csdn.net/beiyus/article/details/51191949?utm_source=blogxgwz3

https://www.dazhuanlan.com/2020/02/28/5e58b9428e9c7/

Groovy 闭包Closure 

https://cloud.tencent.com/developer/article/1407420


https://github.com/google/android-gradle-dsl
https://blog.csdn.net/zhaohad/article/details/104124031


# 参考资料
1. [The Gradle Wrapper](https://docs.gradle.org/5.6.2/userguide/gradle_wrapper.html)
1. [Enum Wrapper.PathBase](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/wrapper/Wrapper.PathBase.html)
2. [](https://blog.csdn.net/u013553529/article/details/55011602)