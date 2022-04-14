[TOC]

修改 Gradle 缓存路径的过程有点曲折记录下。

# 需求
平常用的IDE就两 Android Studio 和 Intellij Idea，而且构建的都是 Gradle 项目，经常切来切去不知道是不是用的同一份缓存的原因，在依赖缓存已经存在于本地的情况下依旧去下载新的依赖，出现该问题次数有点频繁，就想着能不能Android项目和Java项目各用一份依赖缓存？

# 分析

Android 项目和 Java 项目都是 Gradle 构建的，Gradle 默认将 `~/.gradle` 目录作为依赖的缓存目录。缓存目录可以通过环境变量 GRADLE_USER_HOME 来重新指定。

考虑到 Android 项目的编码更加频繁，将 GRADLE_USER_HOME 指向 Android 的依赖缓存路径。 Java 项目则通过其他途径来指定依赖缓存目录。也就是说需要覆盖 GRADLE_USER_HOME 的值，查询 Gradle 官方文档得知：

配置Gradle可以通过以下四种方式(从上至下优先级依次降低)：

1. Command-line flags 命令行参数
2. System properties 系统属性
3. Gradle properties gradle属性
4. Environment variables 环境变量 

由上可知：环境变量优先级最低，命令行参数优先级最高。GRADLE_USER_HOME 属于环境变量优先级最低，先验证下命令行参数方式：

```
gradle -g C:\GradleCache\Java\.gradle build
```

发现依赖缓存存储在 `C:\GradleCache\Java\.gradle` 目录下也就是成功指定了缓存目录命令行参数指定虽然成功，但不方便移植，更期待将缓存路径写入配置文件的方式。

gradle.properties 用于存放系统属性和Gradle属性便于快速构建相同的环境。
相同属性的优先级(从上至下优先级从低到高)由位置所决定：

* Gradle 安装目录的 `gradle.properties` 
* 父项目根目录下的 `gradle.properties`
* GRADLE_USER_HOME 指向的目录下的 `gradle.properties`
* 命令行中的系统属性，例如 `gradle -Dgradle.user.home`

由上可知 gradle.properties 最合适的位置是父项目的根目录。  

根目录新建 `gradle.properties` 文件，粘贴如下配置：

```
systemProp.gradle.user.home=C:\\GradleCache\\Java\\.gradle
```

执行 `gradle build` 命令发现并没有使用指定的目录，`build.gralde` 添加如下Task：

```
task get_gradle_build_config() {
    Gradle var_gradle = project.getGradle()
    println("gradle_home" + var_gradle.gradleHomeDir)
    println("gradle_user_home=" + var_gradle.gradleUserHomeDir)
}
```

根据Task打印的结果发现依旧读取 GRADLE_USER_HOME 的值，后面经过百般猜想测试发现 `gradle.properties` 只对 `gradlew.bat` 和 `gradlew` 有效，于是

```
gradle Wrapper    // convert gradle project to gradle wrapper
gradlew.bat build // use gradle wrapper, not the origin gradle command
```


# 最终方案

使用 Gradle Wrapper，利用 gradle.properties 文件配置依赖缓存的路径。
具体来讲：

* 先Wrapper下 Intellij Idea 构建的Gradle项目
```
gradle wrapper
```
* 新建 gradle.properties 文件新增配置：
```
# this config supply for graldew.bat or gradle shell,in particular it's for
# building project in Terminal
# remeber use gradlew.bat build not gradle build
# because gradle.properties only work on gradle wrapper not gradle
systemProp.gradle.user.home=C:\\GradleCache\\Java\\.gradle
```

* 终端构建，注意是 gradlew.bat 而非 gradle

```
gradlew.bat build
```

# 反思

时间主要花费在分析 `gradle build` 没能读取 `gradle.properties`。  

官方文档并没有明确提出 `gradle.properties` 只对 `gradlew.bat` 和 `gradlew` 起作用
只是想起 Android 项目似乎比 Idea 构建的 Java 项目还要多了一些东西，于是执行 `gradle wrapper`，之后才正常完成了功能。  

中途考虑过在 `build.gradle` 中新建Task动态修改 gradle_user_home, 然后查询API文档后才发现 Gradle 的 gradleHomeDir 和 gradleUserHomeDir 都是只读属性，没办法动态修改，才放弃修改 `build.gradle` 而从配置文件 `gradle.properties` 下手。

# 参考资料
1. [API-Gradle](https://docs.gradle.org/5.6.2/dsl/org.gradle.api.invocation.Gradle.html#org.gradle.api.invocation.Gradle:gradle)
2. [Build Environment](https://docs.gradle.org/current/userguide/build_environment.html)