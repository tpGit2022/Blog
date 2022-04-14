退出需要考虑的因素
1. 可见的界面和不能直接可见的页面
2. 后台开启的service或者线程

一个App打开的activity包括

1.  自身打开的activity
2.  引用的其他第三方库打开的activity

待考虑的情况

1. 正常的退出
2. 应用崩溃的非正常生命周期的退出


暂时收集到的方式

1. 基于基类的收集销毁模拟栈。(被某些人称之为容器式)
    在OnCreate方法中add到List中，在OnDestory中从List中remove
2. 基于基类的BroadCastReceiver
    在基类中添加动态广播接收器，在OnCreate中register，在OnDestory中unregistered，收到退出app的指令时执行finish方法
3. 通过Activity的singleTask的会移除其他activity的特性完成其他activity的finish
4. 直接干掉应用所在的进程
5. 