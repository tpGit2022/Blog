[android需要知道的面试题](http://blog.csdn.net/u013728021/article/details/73743551)  

* SpareArray，该集合为Android的api不是Java的apiLRUCache原理
* 图片加载原理
* 模块化实现（好处，原因）
* 统计启动时长,标准
* 如何保持应用的稳定性
* 动态布局
* 热修复,插件化
* 性能优化,怎么保证应用启动不卡顿
* 怎么去除重复代码
* SP是进程同步的吗?有什么方法做到同步
* 介绍下SurfView
* BroadcastReceiver，LocalBroadcastReceiver 区别
* Bundle 机制
* Handler 机制
* android 事件传递机制
* App启动流程，从点击桌面开始
* 画出 Android 的大体架构图
* 描述清点击 Android Studio 的 build 按钮后发生了什么
* 大体说清一个应用程序安装到手机上时发生了什么；
* 对 Dalvik、ART 虚拟机有基本的了解；
* Android 上的 Inter-Process-Communication 跨进程通信时如何工作的；
* App 是如何沙箱化，为什么要这么做；
* 权限管理系统（底层的权限是如何进行 grant 的）
* 进程和 Application 的生命周期；
* 系统启动流程 Zygote进程 –> SystemServer进程 –> 各种系统服务 –> 应用进程
* recycleview listview 的区别,性能
* Android事件分发机制
* MVP模式
* RxJava
* 消息机制
* 动态权限适配方案，权限组的概念
* 网络请求缓存处理，okhttp如何处理网络缓存的
* 图片加载库相关，bitmap如何处理大图，如一张30M的大图，如何预防OOM
* 进程保活
* listview图片加载错乱的原理和解决方案
* MVP
* 广播（动态注册和静态注册区别，有序广播和标准广播）
* service生命周期
* handler实现机制（很多细节需要关注：如线程如何建立和退出消息循环等等）
* 数据库数据迁移问题
* 是否熟悉Android jni开发，jni如何调用java层代码
* 计算一个view的嵌套层级
* 项目组件化的理解
* 进程间通信的方式
* Android系统为什么会设计ContentProvider，进程共享和线程安全问题
* Android相关优化（如内存优化、网络优化、布局优化、电量优化、业务优化）
* EventBus实现原理
* handler发消息给子线程，looper怎么启动
* View事件传递
* activity栈
* 封装view的时候怎么知道view的大小
* 怎么启动service，service和activity怎么进行数据交互
* 下拉状态栏是不是影响activity的生命周期，如果在onStop的时候做了网络请求，onResume的时候怎么恢复
* view渲染
* singleTask启动模式
* 用到的一些开源框架，介绍一个看过源码的，内部实现过程。
* 消息机制实现
* App启动崩溃异常捕捉
* 事件传递机制的介绍
* ListView的优化
* 模式MVP，MVC介绍
* Android进程分类
* 前台切换到后台，然后再回到前台，Activity生命周期回调方法。弹出Dialog，生命值周期回调方法。
* Activity的启动模式
* RxJava的功能与原理实现
* RecycleView的使用，原理，RecycleView优化
* ANR的原因
* 四大组件
* Service的开启方式
* Activity与Service通信的方式
* Activity之间的通信方式
* Activity与Fragment之间生命周期比较
* 广播的使用场景
* Bitmap 使用时候注意什么？
* Oom 是否可以try catch ？
* 内存泄露如何产生？
* ANR 如何产生？
* 关于handler，在任何地方new handler 都是什么线程下
* sqlite升级，增加字段的语句
* bitmap recycler 相关
* 多进程场景遇见过么？
* Jni 用过么？
* glide 使用什么缓存？
* Glide 内存缓存如何控制大小？
* Activity启动模式
* 广播的使用方式，场景
* App中唤醒其他进程的实现方式
* AndroidManifest的作用与理解
* EventBus作用，实现方式，代替EventBus的方式
* Android中开启摄像头的主要步骤
* Activity生命周期
* AlertDialog,popupWindow,Activity区别
* fragment 各种情况下的生命周期
* Activity 上有 Dialog 的时候按 home 键时的生命周期
* 横竖屏切换的时候，Activity 各种情况下的生命周期
* Application 和 Activity 的 context 对象的区别
* 序列化的作用，以及 Android 两种序列化的区别。
* OOM，内存泄漏
* ANR怎么分析解决
* LinearLayout、RelativeLayout、FrameLayout的特性、使用场景
* 如何实现Fragment的滑动
* ViewPager使用细节，如何设置成每次只初始化当前的Fragment，其他的不初始化
* ListView重用的是什么
* 进程间通信的机制
* AIDL机制
* AsyncTask机制
* 如何取消AsyncTask
* 序列化
* Android为什么引入Parcelable
* 有没有尝试简化Parcelable的使用
* AIDL机制
* 项目：拉活怎么做的
* 应用安装过程
* 简述IPC？
* fragment之间传递数据的方式？
* 内存泄漏的可能原因？
* 用IDE如何分析内存泄漏？
* OOM的可能原因？
* 差值器&估值器
* 简述消息机制相关
* 进程间通信方式？
* Binder相关？
* 触摸事件的分发？
* 简述Activity启动全部过程？
* okhttp源码？
* RxJava简介及其源码解读？
* 性能优化如何分析systrace？
* 广播的分类？
* 点击事件被拦截，但是相传到下面的view，如何操作？
* Glide源码？
* ActicityThread相关？
* 四大组件
* Android中数据存储方式
* 微信主页面的实现方式
* 微信上消息小红点的原理
* RxJava的作用，与平时使用的异步操作来比，优势
* Android消息机制原理
* Binder机制介绍
* 为什么不能在子线程更新UI
* Android中进程内存的分配，能不能自己分配定额内存
* Android事件分发机制
* RxJava的作用，优缺点
* 多线程：怎么用、有什么问题要注意；Android线程有没有上限，然后提到线程池的上限
锁

[Android 复习资料汇总版🔥（更新至20190816）](https://juejin.im/post/5d48e9c36fb9a06af13d50f9)