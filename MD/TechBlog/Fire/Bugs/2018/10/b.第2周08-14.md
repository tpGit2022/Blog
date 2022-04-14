# Bug概要
1. 发生时间:`2018-10-14 10:40:00`  耗时:`xxdxxhxxm`
2. 问题标签 `jd-gui`,`require java runtime 1.7.0`
3. 问题具体描述
   Win10 64位系统已安装jdk 1.9.0 64位，通过 `http://jd.benow.ca/` 下载的jd-gui.exe双击运行提示 `This application requires a Java Runtime Environment 1.7.0` 
4. 错误日志
***日志代码：***
```
This application requires a Java Runtime Environment 1.7.0
```
5. 原因分析
不确定是否只能在1.7.0上运行毕竟该项目已经多年没有更新，google了下有说jdk注册表没有信息的，先看下注册表果然没有相应的信息，手动加上发现虽然没有提示缺少环境依旧打不开。

猜测注册表没有jdk信息导致这个提示, 先看下注册表又没有jdk的信息，查找 `HKEY_LOCAL_MACHINE\SOFTWARE\JavaSoft\Java Runtime Environment` 先完善下注册表 

```
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\JavaSoft]

[HKEY_LOCAL_MACHINE\SOFTWARE\JavaSoft\Java Runtime Environment]
"CurrentVersion"="1.9"

[HKEY_LOCAL_MACHINE\SOFTWARE\JavaSoft\Java Runtime Environment\1.9]
"JavaHome"="D:\\Program Files\\Java\\jdk-9.0.1"
```

> 注意键值中的路径的 `\` 需要转义写成 `\\` 方可正常写入键值

保存如上脚本为 `registerJava.reg`, 双击注册， 之后虽然没有提示需要java环境但没打开成功，只能终端看下有没有错误信息了，`java -jar jd-gui.exe`

先尝试终端 `java -jar jd-gui.exe` 运行，得到错误日志

```
E:\MyCode\ApkDecompiler\0. Tools\jd-gui-windows-1.4.0>java -jar jd-gui.exe
WARNING: An illegal reflective access operation has occurred
WARNING: Illegal reflective access by org.codehaus.groovy.reflection.CachedClass$3$1 (file:/E:/MyCode/ApkDecompiler/0.%20Tools/jd-gui-windows-1.4.0/jd-gui.exe) to method java.lang.Object.finalize()
WARNING: Please consider reporting this to the maintainers of org.codehaus.groovy.reflection.CachedClass$3$1
WARNING: Use --illegal-access=warn to enable warnings of further illegal reflective access operations
WARNING: All illegal access operations will be denied in a future release
Exception in thread "main" java.lang.reflect.InaccessibleObjectException: Unable to make jdk.internal.loader.ClassLoaders$AppClassLoader(jdk.internal.loader.ClassLoaders$PlatformClassLoader,jdk.internal.loader.URLClassPath) accessible: module java.base does not "opens jdk.internal.loader" to unnamed module @53f65459
```


搜索得到相关issue `https://github.com/java-decompiler/jd-gui/issues/187`根据提示终端输入
```
java --add-opens java.base/jdk.internal.loader=ALL-UNNAMED --add-opens jdk.zipfs/jdk.nio.zipfs=ALL-UNNAMED -jar jd-gui.exe
```

运行jd-gui.exe成功考虑到使用较为频繁，索性编写批处理脚本 `jd.bat` 来使用

```
@echo off
java --add-opens java.base/jdk.internal.loader=ALL-UNNAMED --add-opens jdk.zipfs/jdk.nio.zipfs=ALL-UNNAMED -jar jd-gui.exe
```

之后双击 jd.bat 即可运行 jd-gui.exe

6. 解决方案
***解决方案代码:***
```
@echo off
java --add-opens java.base/jdk.internal.loader=ALL-UNNAMED --add-opens jdk.zipfs/jdk.nio.zipfs=ALL-UNNAMED -jar jd-gui.exe

```
7. 参考资料
   https://github.com/java-decompiler/jd-gui/issues/187
8. 反思和总结