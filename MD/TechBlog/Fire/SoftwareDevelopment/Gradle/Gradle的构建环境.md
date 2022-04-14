[TOC]

update:2019.09.25
这篇更像是译文，大部分内容来至 https://docs.gradle.org/current/userguide/build_environment.html

# 前言

Gradle 可以通过多种途径来配置Gradle本身和项目的行为，以下具体的途径：

1. Command-line flags: 命令行参数，例如： `gradle -g cacheDirPath`
2. System properties：系统属性，系统属性以 `systemProp.` 作为前缀
3. Gradle properties： Gradle属性
4. Environment variables：环境变量

***优先级从上至下依次降低***  

**System properties** 和 **Gradle properties** 均可存放于 **gradle.properties** 文件中

# Command-line flags

以下可用作命令参数的选项：

| 简写 | 全名 | 作用 | 实例 |
|:--|:--|:--|:--|
| -b | --build-file | 指定构建文件，默认值是 `build.gradle` 或者 `build.gradle.kts` | `gradle -b custom_build.gradle` |
| -c | --settings-file | 指定 settings 文件, 默认是 `settings.gradle` | `gradle -c` |
| -g | --gradle-user-home | 指定依赖存储目录 | `gradle -g C:\GradleCache\.gradle` |
| -p | --project-dir | 指定开始的目录，默认是当前目录 | |
| -D | --system-prop | 配置JVM的系统属性 | `gradle -DFileEncoding=UTF-8` |
| -I | --init-script | 指定初始化脚本 | |
| -p | --project-prop | 指定项目属性 | |
|| -Dorg.gradle.jvmargs |  设置JVM虚拟机参数 | |
|| -Dorg.gradle.java.home | 设置JDK路径 | |


# 属性(Gradle properties 和 System properties)  

命令行参数的方式虽然优先级最高但不利于快速构建，将属性放置 **gradle.properties** 中是更有效的方式。该文件的位置决定了属性的优先级，常见存放位置如下:

1. Gradle 安装目录下的 **gradle.properties**  
2. 父项目根目录下的  **gradle.properties**  
3. 环境变量 GRADLE_USER_HOME 指向的目录下的  **gradle.properties**  
4. 命令行中配置的系统属性

***从上至下优先级依次增大***  
常用的 Gradle 属性(Gradle properties) 如下：

| 属性名 | 取值 | 作用 |
|:--|:--|:--|
| org.gradle.caching | true, false | |
| org.gradle.caching.debug | true,false ||
| org.gradle.configureondemand | true,false ||
| org.gradle.console | auto,plain,rich,verbose ||
| org.gradle.daemon | true,false ||
| org.gradle.daemon.idletimeout | # of idle millis | |
| org.gradle.debug | true,false ||
| org.gradle.java.home | path to JDK home ||
| org.gradle.jvmargs | JVM arguments ||
| org.gradle.logging.level | quiet,warn,lifecycle,info,debug ||
| org.gradle.parallel | true,false ||
| org.gradle.warning.mode | all,none,summary ||
| org.gradle.workers.max | max # of worker processes ||
| org.gradle.priority | low,normal | |

系统属性(System properties) 在命令中需要加上 `-D`, 而在 **gralde.properties** 中需要加上前缀 `systemProp.`。  
常用的一个系统属性是 **gradle.user.home**  

***多项目中只有父项目gradle.properties的系统属性才有用***  

常见的属性配置gradle.properties内容如下:

```
org.gradle.daemon=false
org.gradle.jvmargs=-Xmx16384m -XX:MaxPermSize=512m -XX:-UseGCOverheadLimit -XX:+HeapDumpOnOutOfMemoryError -Dfile.encoding=UTF-8
org.gradle.parallel=true
org.gradle.configureondemand=true
org.gradle.warning.mode=all
#systemProp.http.proxyHost=127.0.0.1
#systemProp.http.proxyPort=8080
#systemProp.https.proxyHost=127.0.0.1
#systemProp.https.proxyPort=8080
# this config supply for graldew.bat or gradle shell,in particular it's for
# building project in Terminal
# remeber use gradlew.bat build not gradle build
# because gradle.properties only work on gradle wrapper not gradle
systemProp.gradle.user.home=C:\\GradleCache\\Java\\.gradle
```

# 环境变量(Environment variables)

可用的环境变量有三个：

* ***GRADLE_OPTS***
配置 Gradle client VM 的参数

* ***GRADLE_USER_HOME***  
指定 Gradle 缓存依赖的目录， 默认是 `~/.gradle`

* ***JAVA_HOME***
指定JDK的安装目录

# 项目属性（Project properties)

# 配置 JVM 内存(Configuring JVM memory)

这里指的 JVM 指的 Gradle的守护进程Daemon的JVM设置，守护进程的设计本身是为了加快构建流程。  

gradle.properties 的JVM配置是为守护进程配置的，默认的配置如下:  

```
# Default value: -Xmx1024m -XX:MaxPermSize=256m
#org.gradle.jvmargs=-Xmx2048m -XX:MaxPermSize=512m -XX:+HeapDumpOnOutOfMemoryError -Dfile.encoding=UTF-8
```

为了加快构建的流程，在内存充足的情况下尽可能的为守护进程的JVM配置大内存

`Xmx`:堆最大内存值，单位m，g均可
`-XX:MaxPermSize`:设置持久代最大内存值，1.8后被弃用
`-XX:MaxMetaspaceSize`:设置持久代的最大内存值，1.8后用于取代-XX:MaxPermSize
`-XX:+HeapDumpOnOutOfMemoryError`:发送内存溢出时保存快照
``:



https://www.cnblogs.com/zhi-leaf/p/10627949.html

8G 常用虚拟机配置

16G 常用虚拟机配置

32G 常用虚拟机配置

`org.gradle.jvmargs=-Xmx8192m -XX:MaxPermSize=2048m -XX:+HeapDumpOnOutOfMemoryError -Dfile.encoding=UTF-8`


# Task中使用项目属性 (Configuring a task using project properties)

# 使用代理 (Accessing the web through a HTTP proxy)

在 gradle.properties 文件添加如下代码即可使用代理：
HTTP

```
systemProp.http.proxyHost=www.somehost.org
systemProp.http.proxyPort=8080
systemProp.http.proxyUser=userid
systemProp.http.proxyPassword=password
systemProp.http.nonProxyHosts=*.nonproxyrepos.com|localhost
```

HTTPS

```
systemProp.https.proxyHost=www.somehost.org
systemProp.https.proxyPort=8080
systemProp.https.proxyUser=userid
systemProp.https.proxyPassword=password
systemProp.https.nonProxyHosts=*.nonproxyrepos.com|localhost
```

# 参考资料
1. [Gradle-Docs-Build Environment](https://docs.gradle.org/current/userguide/build_environment.html)