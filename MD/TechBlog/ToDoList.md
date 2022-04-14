TODOLIST

# JNI开发
* 第一阶段了解总体流程步骤，知道总体流向，最好单独的编译，运行。环境的搭建，编译，运行均在此列，这一部分主要在于记忆，不需要执着于细节
* 了解个流程具体的开发细节，输入与输出

# Gradle



当前的JNI的了解。JNI(Java native interface)的缩写，用于java调用原生代码即c或者cpp文件，在windows上面调用的是dll文件，在Linux上面调用的so文件，所有在Android上面调用的是so文件。

JNI在java层面是用native 修饰的方法，通过system.load.library载入原生库。产生问题

一：如何在执行过程中进行java层和native层通信，当前所知道的只是java层调用native，相反native是否可以调用java层面，如果可行如何调用。
二:java和调用native代码是否处于同一线程，是否处于同一进程。window或者Linux层使用有线程这一说。
三:java层次调用native代码需要传递参数，native返回值给java层，在java层 和native层的类型如何对应，以及是否可以加载多个so文件，多个文件中的so文件方法名重复如何解决
四：还是通信问题，native方法的同步，如果native方法层新开了线程进行操作如何保证java层得到的返回值是真正的返回值而不是native初始化的尚未进行操作的返回值
五：c/c++ 的数据类型的取值和java层面并非一直，如何保证数据的正确性？

dll功能性的验证，native代码的调试


决定用于练手的Android层的JNI实际小项目：
1. Android层调用C层的各类排序算法
2. Android层调用C层fork新进程，达到进程保活目的。


Oracle官方关于分析Java错误日志的文档。
https://docs.oracle.com/javase/8/docs/technotes/guides/troubleshoot/crashes001.html

https://docs.oracle.com/javase/8/docs/technotes/guides/troubleshoot/toc.html

小而明确的执行目标：

* CMakeList.txt
  输出:CMake解析文章和Demo

* Android.mk,Application.mk的写法
  输出：Android.mk,Application.mk的写法的文章和Demo

* Android Platfrom Tools子目录
    - adb, appt, sqlite3 fasttool
* adb命令总览
    - 输出 adb命令文章和实例最后可以有个实际用途的shell script

* am命令， pm命令
* 辅助服务自动化插件



adb shell dumpactivity

Stack
Task id
TaskRecord



暗号启动app，launch不显示应用图标
参考资料
https://www.jianshu.com/p/fa1143cf1b0f
http://androidxref.com/7.1.2_r36/xref/packages/services/Telephony/src/com/android/phone/SpecialCharSequenceMgr.java

基本原理：
拨号键盘中输入`*#*#code*#*#`(code为任意可输入内容)系统会发生一个BroadCast。app接收这个broadcast启动app的界面即可达到该效果。具体的逻辑可以在**SpecialCharSequenceMgr.java** ， 


Android中相关功能点
应用功能层面：
LBS(地理定位)
Sensor(传感器)
Wifi-Bluetooth(无线技术)：局域网快传和蓝牙通信
桌面组件(Remote View)
WebView()
通知，闹钟(Notification,AlarmManager)
界面锁屏，图形锁，数字锁。
ContentProvider(日历，。联系人，短信)
Activity
Fragment
Broadcast
Intent
IntentFilter
PendingIntent
应用信息获取Pm
图片图像处理
复制粘贴
拖拽功能
Android Debug 工具。
RecycleView


大层面

1. 计算机网络
2. 数据结构，算法
3. Android应用层开发
4. Android系统层
5. Python爬虫
6. 数据库操作。
7. JS操作


编程语言
Java
Koltin
Python
JavaScript


各种乱七八糟应该做的事情。

Python层
春恋爬虫
Re爬虫
跌荡一百年上下爬虫


Java层

Android层
开发常用库(GreenDAO,Dagger2):层次
华为运动健康反编译-数据获取
应用定时器数据-数据获取
sqlite3命令语法
Google Docs


Koltin层

JavaScript层

Linux层
全局代理使用

数据库
库子清洗rebuild
SQL语法


时间统计：
1. 华为健康数据
2. wakatime数据
3. 手机app-应用定时器


无侵入式统一替换ImageView为黑白灰色模式