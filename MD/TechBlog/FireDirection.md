[TOC]

# 开发
1. Java
2. Android
	1. 自动化测试：
      1. UiAutomator		
      2. Monkey		
      3. MonkeyRunner
    2.  第三方框架
     1. Okhttp，Retrofit
     2. EventBus
     3. BufferKinfe



# 脚本
1. DOS批处理脚本
2. svn
3. git
4. Python
5. JavaScript

# 系统
1. Linux
  1. Ubuntu
  2. Kali Linux

# 开发软件
1. Android Studio		
2. Eclipse		

# 编辑器
1. Vim		
2. Atom
3. Sublime_text 3
4. Windows Live Write

# 常用软件
1. WireShark
2.

# 小Demo
MarkdownPic 图片处理器


方向：


* Gradle  

达成目标：  
1. 打包的多种buildType,Flavor --> apk的存放位置，apk名称，版本号以及类型变量  
2. 清楚大致的 Gradle 构建流程
3. 略有涉及 gradle-plugin 的编写

* 自定义View  

以前看的自定义View都快忘记的差不多了，在重温一次，依据HenCoder扔物线的Blog在熟悉一次，重点侧重于

* 整体自定义View/ViewGroup的流程，两者的区别和联系
* Paint 的常用方法
* Canvas 的常用方法
* 矩阵变换，贝塞尔曲线

自定义View需要注意的问题：不影响原来的属性的设置譬如：wrap_content，match_parent属性以及为控件设置的background的drawable对象，padding，margin等等属性需要依旧保持正常

思考一下几个问题：
1. 自定义View/ViewGroup中的onDraw方法中调用getWidth()和getHeight()是否包含了margin，padding。  
2. 当屏幕发生旋转是Android的视图坐标轴有什么变化，X和Y值分别会变化为什么
3. Android视图坐标系中Z轴是什么，有什么用


权限管理类
屏幕录制类 https://www.cnblogs.com/liushilin/p/11086697.html  
https://github.com/nanchen2251/ScreenRecordHelper

网络请求相关 无数据，出错了的统一页面处理 记得公开的库子可用