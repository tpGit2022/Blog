[TOC]

Android的AccessibilityServices，AccessibilityServices中文一般被翻译为无障碍服务。Google用于为诸如视力不好，听力不够的人特意设计的使用的。通过这项服务开发者可以为存在功能障碍的人士开发具备语音反馈，震动反馈以及手势识别等等辅助功能的应用，方便他们的使用。

*When setting up your accessibility service, carefully consider what events your service is able to handle and only register for those events. Since users can activate more than one accessibility services at a time, your service must not consume events that it is not able to handle. Remember that other services may handle those events in order to improve a user's experience.*

> *Note: The Android framework dispatches accessibility events to more than one accessibility service if the services provide different feedback types. However, if two or more services provide the same feedback type, then only the first registered service receives the event*

当多个AccessibilityServices注册了同种事件，如果提供的反馈方式也是一致的，只有先注册的Services可以接收到Android系统分发的事件。
建立一个AccessibilityService的基本流程:
1. 继承AccessibilityService类，override重写两个必须实现的onAccessibilityEvent和onInterrupt方法
2. 在清单文件中添加权限以及服务的说明。
3. 在OnAccessibility根据接到的`AccessibilityEvent`实例先通过text或者控件id查找需要的控件再执行动作Action

Using focus types

Android 4.1 (API Level 16) introduces a new type of user interface focus called Accessibility Focus. Accessibility services can used this type of focus to select any visible user interface element and act on it. This focus type is different from the more well known Input Focus, which determines what on-screen user interface element receives input when a user types characters, presses Enter on a keyboard or pushes the center button of a D-pad control.

Accessibility Focus is completely separate and independent from Input Focus. In fact, it is possible for one element in a user interface to have Input Focus while another element has Accessibility Focus. The purpose of Accessibility Focus is to provide accessibility services with a method of interacting with any visible element on a screen, regardless of whether or not the element is input-focusable from a system perspective. You can see accessibility focus in action by testing accessibility gestures. For more information about testing this feature, see Testing gesture navigation.

Note: Accessibility services that use Accessibility Focus are responsible for synchronizing the current Input Focus when an element is capable of this type of focus. Services that do not synchronize Input Focus with Accessibility Focus run the risk of causing problems in applications that expect input focus to be in a specific location when certain actions are taken.

An accessibility service can determine what user interface element has Input Focus or Accessibility Focus using the AccessibilityNodeInfo.findFocus() method. You can also search for elements that can be selected with Input Focus using the focusSearch() method. Finally, your accessibility service can set Accessibility Focus using the performAction(AccessibilityNodeInfo.ACTION_SET_ACCESSIBILITY_FOCUS) method

译文:
为用户采取Action的方式三：通过使用Focus Type。
在API 16即Android4.0,引入了一种新的称之为Accessibility Focus的的Focus类型，通过新的Focus Type，Accessibility Services可以找到用户界面上任何可见的元素并且执行动作(Action)，

Accessibility Focus完全不同于Input Focus

可以添加的xml属性

| XML attributes | Meannins |
|:---|:--|
| android:accessibilityEventTypes | 用于决定接受那些类型的事件是点击事件还是获取焦点事件等，多个标记用`|`分割
| android:accessibilityFeedbackType | 决定反馈的类型比如震动反馈或者语音反馈，多个标记用`|`分割
| android:accessibilityFlags | 标记，多个标记用`|`分割
| android:canrequestEnhancedWebAccessibility | 是否具备
| android:canRequestFilterKeyEvents | 
| android:canRequestTouchExplorationMode | 
| android:canRetrieveWindowContent |
| android:description 	| 
| android:notificationTimeout |
| android:packageNames 	| 用于决定哪些包名被监听，多个包名用`,`分割
| android:settingsActivity | 用于设置AccessibilityServices的界面。

需要重点掌握的几个类。
![20170105210827.png](../../../../../Pictures\20170105\20170105210827.png)  
通过`startService(intent)`虽然可以启动辅助服务，能看见辅助服务的`OnCreate`,`OnStartCommand` 方法被执行。但`onAccessibilityEvent`以及`onInterrupt`并不会被执行，只有手动开启了辅助服务功能之后`onAccessibilityEvent`以及`onInterrupt`才会被正常的回调，执行处理逻辑。

# 参考资料

1. [徐宜生-AccessibilityService从入门到出轨](http://www.myzaker.com/article/586653e51bc8e0a341000001/)
2. [360关于Android的AccessibilityService的安全性研究](http://www.freebuf.com/articles/terminal/114045.html)
3. https://developer.android.google.cn/guide/topics/ui/accessibility/index.html
4. https://developer.android.google.cn/guide/topics/ui/accessibility/services.html