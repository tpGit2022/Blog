方案
监听系统卸载广播：只能监听到其他应用的卸载广播，无法监听到自己是否被卸载。
读取系统 log：第三方软件卸载无法得知。
静默安装另一个程序，监听自己是否被卸载：需要 root 权限。
Java 线程轮询，监听/data/data/{package-name}目录是否存在：卸载 app，进程退出，线程也被销毁。
C 进程轮询，监听/data/data/{package-name}目录是否存在：目前业界普遍采用的方案。
原理
从前四种方案可以看到，单纯的 Java 层代码是无法监听自身卸载的。既然 Java 层无法实现，我们试着使用 C 语言在底层实现。借助 Linux 进程 fork 出来的 C 进程在应用被卸载后不会被销毁，监听/data/data/{package-name}目录是否存在，如果不存在，就证明应用被卸载了。
本程序采用第 5 种解决方案，对其进行优化，通过 linux 中的inotify机制来监听应用的卸载。
实现
fork()子进程
创建监听文件
初始化 inotify 实例
注册监听事件
调用 read 函数开始监听
卸载反馈统计
场景
正常卸载
断网卸载
清除数据（5.0 以上不支持）
kill 进程（5.0 以上不支持）
插拔 USB 线
覆盖安装
内部存储移到 SD 卡
开机监听（官方不推荐）
打开浏览器（5.0 以上部分机型无法开启）


# 参考资料
1. [ Android App 监听自身卸载，反馈统计](http://blog.csdn.net/u014608640/article/details/53080508)
2. [Android应用如何监听自己是否被卸载及卸载反馈功能的实现（第二版）](http://www.cnblogs.com/zealotrouge/p/3159772.html)
3. [Android NDK开发(八)——应用监听自身卸载，弹出用户反馈调查](http://blog.csdn.net/allen315410/article/details/42521251)