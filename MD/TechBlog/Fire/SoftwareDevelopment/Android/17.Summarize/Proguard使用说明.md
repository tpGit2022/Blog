代码混淆(Code Obfuscation):将代码中的类名，方法，字段等成员变为无意义的a,b,c,d,f等名称增加代阅读分析的难度。

Proguard 是一项工具，首先代码混淆(Code Obfuscation)只是它的功能之一。
***Proguard是一个压缩(Shrink)，优化(Optimize)，混淆(Obfuscation)Java字节码的工具***  
其执行过程也是Shrink-Optimize-Obfuscation，大流程如下图：  

![summary](../../../../Pictures\20180116\20180425101220.png)

Shrink:主要检查并剔除没有使用的类，字段，方法和属性
Optimize:分析优化方法的二进制码
Obfusccation:将被保留下来的类，字段，方法使用短的没有意义的名称来替代。

> Proguard其实还有第四部预校验Preverify， 但Android一般会关闭该项以加快混淆速度

先来了解几个概念：
**Entry Point**  锚点，简单来讲就是Proguard会保留的代码，在Doc中`seed`也表示同样的意思。

`keep`等多个关键字的选项是为了避免类和成员被Shrink，Obfuscation。如果开启了不Shrink的规则，那么所有的类和成员都不会被移除。
```
# 不要移除资源
-dontshrink
```

`-keep [,modifier,...] class_specification`

***Specifies classes and class members (fields and methods) to be preserved as entry points to your code***  

个人翻译为：将符合条件的类和类的成员作为接入点而保留。

`-keepclassmembers [,modifier,...] class_specification`

***Specifies class members to be preserved, if their classes are preserved as well***  

个人翻译为：在类被保留的情况下，符合条件的类的成员也将被保留

`-keepclasseswithmembers [,modifier,...] class_specification`

***Specifies classes and class members to be preserved, on the condition that all of the specified class members are present.***  

个人理解为：只有符合所有条件才会保留类和类的成员。



从上可以看出在整个过程中中类和成员被压缩或者重命名，为了下文叙述方便约定名称：
* 类移除：指整个类包括成员被压缩删除掉了
* 类保留：指整个类包括成员既没有被压缩也没有被重命名
* 类名保留：


类移除
类保留
类名保留
类名移除

成员移除
成员保留



先弄清楚第一层问题
```
1. 为什么要混淆？
2. 那些需要混淆，那些需要保留，如何保留？
3. 混淆后的代码出错了如何调试
```

混淆针对的是类，类的成员无非变量和方法。


混淆产生的映射表每次都相同吗？有什么规律

常用的几个关键字
`keep` 用法 `-keep [,modifier,...] class_specification`

***modifier***  
includedescriptorclasses

includecode

allowshrinking

allowoptimization

allowobfuscation

***class_specification***  

![class_specification](../../../../Pictures\20180116\20180419170834.png)

常见的几种用法。
1. 保留某个类所有变量和方法 `-keep class com.xxx.xxx.classname {*;}`
2. 保留类名 `-keep class com.xxx.xxx.classname`
3. 

`keepattributes`
`keepclasseswithmembernames`
`keepclasseswithmembers`
`keepclassmembernames`
`keepclassmembers`
`keepnames`
`keeppackagenames`
`keepparameternames`



各个`keep`关键字的联系和区别：
![keep connect and difference](E:\MyBlogs\TechBlog\Pictures\20180116\20180424100436.png)


![modify](../../../../Pictures\20180116\20180424100758.png)


```
If you're not sure which option you need, you should probably simply use -keep. It will make sure the specified classes and class members are not removed in the shrinking step, and not renamed in the obfuscation step.
```


`keep` 和 `keepclassmember`的区别在于，后者如果指定的类没有被用到

类名 被移除 或者改名
变量名 被移除 或者改名
方法被移除 或者改名

https://www.guardsquare.com/en/proguard/manual/usage#allowshrinking

六个关键字
`keep,keepclassmembers,keepclasseswithmembers,keepname,keepclassmembersname,keepclasseswithmembersname`,前三者为一类，后三者为一类，后三者本质上是前三者加上了`allowshrinking`修饰符(modifier)的.

前三者使用方式一致：
`-keep [,modifier,...] class_specification`

后三者使用方式一致：
`-keepname class_specification`

> `-keepname class_specification` 是`-keep ,alloshrinking class_specification`的简化



几个关键字的用法如下：
1. `keep`
usage:`-keep [,modifier,...] class_speciffication`
中括号代表非必要参数，实际例子如下：
`-keep ,allowshrinking class com.example.administrator.testsdk.bean.Cat {}`

> modifier 和keep关键字间需要空格和逗号`,`只有空格会出错，多个modifier之间逗号隔开，后面的class_specification是必要项，代表着要keep的类的模板。


`keep` 即便指定的类没有被使用也保留
`keepclassmember` 只有当该类被使用过且符合时才会保留符合的成员变量，但类名还是会被混淆
`keepclasseswithmember` 即便该类没有被使用过，只要符合也保留类名，

对代码而言主要关注的变化的只有两点：
1. 类是否被移除，类名是否会被重命名
2. 类的成员变量是否会被移除，是否会被重命名。

`keep`:保留类和类名
`keepclassmembers`:如果符合条件的类存在则保留该类的成员变量
`keepclasseswithmembers`:如果符合该类的条件存在则保留该类的成员变量和类名

开启混淆后`build/outputs/mapping/release`目录下会产生四个文件
* dump.txt:列出描述apk文件中所有类文件间的内部结构
* mapping.txt:列出原始类，方法，字段和混淆后代码之间的映射
* seeds.txt:列出没有被混淆的类和成员
* usage.txt:列出从apk中删除的代码

# 参考资料
1. [Google Docs - Code Obfuscation](https://developer.android.google.cn/studio/build/shrink-code.html?hl=zh-cn)
2. [Proguard Docs](https://www.guardsquare.com/en/proguard/manual/introduction)
3. [proguard混淆](https://www.jianshu.com/p/3d89e3c2a081)


| Factor/Result | Shrink | Class Quote | Member Quote | Class Result | Member Result |
|:--:|:--:|:--:|:--:|:--:|:--:|
| keep | | | |
| keepclassmembers | | | |
| keepclasseswithmembers | | | |
| keepnames | | | |
| keepclassmembernames | | | |
| keepclasseswithmembernames | | | |


* keep

Shrink 

Quote 类名保留，符合规则的成员被保留，否则根据是否被引用，引用的被重命名否则被移除

No Quote 类名保留，符合规则的成员被保留，其他成员被移除

DontShrink

Quote 类名保留，符合规则的成员保留，否则被重命名

NoQuote 类名保留，符合规则的成员保留 其他成员被重命名

* keepclassmember

Shrink

Quote 类被重命名，符合规则的成员被保留，否则根据是否被引用，被引用重命名，否则被移除
NoQuote
没有被引用，直接移除该类。

NoShrink
类被重命名，符合条件的成员被保留，否则被重命名


* keepclasseswithmember

Shrink
Quote  符合所有模板条件，类名被保留，符合条件的成员名也被保留，其他被引用的成员被重命名。不符合同一条`keepclasseswithmember`中模板条件之一，类被重命名，有引用的成员被重命名，没有引用的成员被移除。
NoQuote

符合所有模板条件 类名被保留，符合条件的成员名被保留，不符合同一条`keepclasseswithmember`条件之一，类被移除。

DontShrink
Quote 符合所有模板条件，类名保留，符合条件的成员保留成员名，不符合则保留成员
    不符合同一条语句条件之一，类名移除，成员名移除
NoQuote 
    符合所有模板条件，类名保留，符合条件的成员保留成员名，不符合则保留成员
    不符合同一条语句条件之一，类名移除，成员名移除
    
移除类         保留类名       
移除成员       保留成员名     
移除类名       保留类
移除成员名     保留成员


# ���考资料
1. [ProGuard代码混淆详细攻略](https://blog.csdn.net/shensky711/article/details/52770993)


