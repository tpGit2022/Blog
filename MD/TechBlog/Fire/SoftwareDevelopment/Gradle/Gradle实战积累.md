1. 刷新依赖`gradle build --refresh-dependencies`
2. 查看当前项目所有的task
```
gradle tasks
```

3. 指定本地缓存的目录
* `gradle -g cacheDirPath taskName`


通过命令行-g或者 --gradle-user-home 参数设置

法1.通过添加系统变量 GRADLE_USER_HOME
法2.设置虚拟机参数 org.gradle.user.home 属性


https://blog.csdn.net/yanzi1225627/article/details/52024632


-g, --gradle-user-home    Specifies the gradle user home directory.


Gradle 是构建项目的工具，使用基于JVM的Groovy语言进行配置。构建中最重要的是
`build.gradle` 和 `settings.gradle`两份文件，前者对应着project，后者描述了多项目间的关系。属性 `rootpoject`描述的是最顶层的build.gradle所在位置。**project** 获取的则是当前build.gradle所指的项目。

依赖的描述 group:name:version 写法上有两种

```
compile groupname:dpname:version
或者
compile group : 'groupname', name : 'name', version : 'versionNum'
```


多模块描述上用 `:`分割，执行特定目录下的子项目如 **A/B/C** 的c项目  ，可以切换至该项目下执行`gradle taskname` 或者 直接在A的目录下执行`gradle :A:B:C taskname`


https://www.jianshu.com/p/ec517bb2fcfa


只产生编译特定平台的so文件在`build.gradle`中的`android`节点添加
```
ndk {
            abiFilters "armeabi-v7a"
}
```

> 上述配置只会在apk的lib中产生armeabi-v7a平台

没有配置时产生全平台，`x86,x86_64,arm64-v8a,armeabi-v7a`

CMake 修改生成本地库的名称是需要同步修改 add_library节点和target_link_libraries

# Gradle查看项目的依赖
```
gradlew.bat -q dependencies projectname:dependencies
```

输出项目总依赖关系(包括子项目)
builg.gradle添加
```
subprojects {
    task allDeps(type: DependencyReportTask) {}
}
```

终端执行：
`gradlew.bat allDeps`

# 排除某个依赖
```
exclude group: 'com.android.support', module: 'support-v4'
```
从所有依赖中排除某个依赖
```
configurations {
        compile.exclude group: 'com.android.support', module: 'support-v4'
}
```
Android中将上述代码添加至顶层的build.gradle的allproject节点下。


# 存在多个版本的依赖如何确定？
同一个依赖的不同表现形式，优先级那个最高，不同依赖之间如何取舍？


# Gradle项目编译报错：编码GBK的不可映射字符  
  项目一开始是GBK的后面改成了UTF-8，执行打包JAR时一直提示编码不可映射，查看生成
的JAR包发现class文件是GBK的，无奈搜索得到如下连接：
https://blog.csdn.net/dknightl/article/details/79950305

修改了 build.gradle 编码依旧没得效果，添加 `tasks.withType(JavaCompile) {options.encoding = 'UTF-8'}` 才正常了



groovy 语言中文文档
http://cndoc.github.io/groovy-doc-cn/

test

# so库的选择

so库的参数是有CPU架构的不同，通过如下命令即可查看cpu的架构：  

`adb shell getprop ro.product.cpu.abi`

常见的so库的类型有 `mips, mips64, X86, X86–64, arm64-v8a, armeabi, armeabi-v7a`

目前占有的市场率是arm64-v8a-->armeabi-v7a-->armeabi-->x86,x86-64

其中 x86和x86-64占据的市场在百分之一左右，基本不用考虑，除非app设计需要在模拟器上运行，因为模拟器都是x86的结构

so库的查找顺序如下：  
![so库搜索顺序](E:\\MyIT\\MyBlogs\\TechBlog\\Pictures\\20200112\20200605194311453.png)

so库找不到的常见异常：  

```
Exception:Java.lang.UnsatisfiedLinkError: dlopen failed: library “/***.so” not found 
```

https://blog.csdn.net/whbk101/article/details/101775032  

https://blog.csdn.net/xx326664162/article/details/51167849  

https://juejin.im/post/5eae6f86e51d454ddb0b3dc6

