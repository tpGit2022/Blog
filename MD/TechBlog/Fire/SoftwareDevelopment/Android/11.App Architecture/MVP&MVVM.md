# MVP
Model-View-Presenter。MVP模式中包含3个基本要素
1. View：负责绘制UI元素，进行用户交互
2. View interface：View需要实现的接口，View通过View interface与Presenter进行交互
3. Model：负责存储，检索，操纵数据
4. Presenter：View和Model交互的中间纽带，负责处理逻辑
**MVP的优点**  
1. 模型与视图的完全分离，耦合度降低，更容易专注业务逻辑，便于维护，项目结构清晰
2. 将逻辑放在Presenter，Presenter层不使用Android API，纯java代码便于后期的单元测试。

**MVP的缺点**  
1. 通常View和Presenter时一对一的(复杂的View可能绑定多个presenter来处理逻辑)，增大代码量
2. 对View的渲染均放在了Prsenter中，View和Presenter交互频繁。

Demo中的代码结构：  
![20170525202057.png](../../../../Pictures\20170525\20170525202057.png)  

Demo模拟的功能：点击按钮-获取数据-展示数据。


# MVVM
Model-View-ViewModel。

通过数据绑定DataBinding，View的变化直接影响ViewModel，ViewModel的的变化或者内容也会直接体现再View上。
与MVP模式最大的不同在于View和中间层Presenter(ViewModel)的交互，在MVP的模式中，View实现视图更新的接口给Presenter调用，Presenter在有需要的时候调用View更新视图的接口，而MVVP模式中，View和View Model的变化自动相互影响，View的变化自动反应在View Model中，ViewModel的数据变化也自动反应在View中，在Android中MVVP的数据绑定DataBind是通过Google官方的数据绑定框架DataBinding(当然也有其他数据绑定框架比如RoboBinding)。目前Google的DataBinding算不上稳定成熟，不是很推荐MVVM模式，这里就不展开叙述。

# 参考资料
1. [Android App的设计架构：MVC,MVP,MVVM与架构经验谈](https://www.tianmaying.com/tutorial/AndroidMVC)
2. [维基百科MVVM](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93viewmodel)
3. [AndroidMVVM](https://github.com/wtopolski/androidmvvm)
4. [Android MVP 详解](http://www.jianshu.com/p/9a6845b26856)
5. [Android MVP开发模式的结构及优缺点详解](http://www.maiziedu.com/article/8549/)
6. [Android App的设计架构：MVC,MVP,MVVM与架构经验谈](https://www.tianmaying.com/tutorial/AndroidMVC)
7. [[Android] MVVM设计模式及实例](http://blog.qiji.tech/archives/7722)
8. [Android MVVM到底是啥？看完就明白了](https://juejin.im/entry/56781baf00b01b78ac54c10a)
9. [Android官方MVP架构示例项目解析](http://www.infoq.com/cn/articles/android-official-mvp-architecture-sample-project-analysis)
10. [Google官方MVPDemo](https://github.com/googlesamples/android-architecture/tree/todo-mvp/)
11. [Google官方MVVMDemo](https://github.com/googlesamples/android-architecture/tree/todo-mvvm-databinding/)