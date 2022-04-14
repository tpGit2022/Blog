
`This class represents the basic building block for user interface components. A View occupies a rectangular area on the screen and is responsible for drawing and event handling`

大致意思是：
视图(View)是创建用户界面组件的基本构件，View在屏幕中占据一个矩形区域，负责该区域的绘制和事件的处理。

# 自定义View
自定义View时有些方法是被常被复写的。

| 分类 | 方法 | 作用 |
|:---:|:--:|:--:|
| Creation | Constructors | 构造方法 |
| Creation | onFinishInflate | 当所有View和子View均被渲染完后被调用 |
| Layout | onMeasure | 测试尺寸，决定了View以及子View的尺寸 | 
| Layout | onLayout | 自定义ViewGroup会复写的方法用于决定子View摆放的位置 |
| Layout | onSizeChanged | 当View的尺寸发生变化时被调用 | 
| Drawing | onDraw | 用于绘制View的内容 |
| Event Processing | onKeyDown |  |
| Event Processing | onKeyUp | |
| Event Processing | onTrackballEvent | 轨迹球滑动时被调用 |
| Event Processing | onTouchEvent | 发生触摸事件时被调用 |
| Focus | onFocusChanged |  当View获取焦点或者失去焦点时被调用 |
| Focus | onWindowFocusChanged | 当包含该View的windows获取或者失去焦点时被调用 |
| Attaching | onAttachedToWindow | 当View被附到windows时被调用 |
| Attaching | onDetachedFromWindow | 当View从windows时上移除时被调用 |
| Attaching | onWindowsVisibilityChanged | 当windows包含的View或者子View的可见性发生变化时被调用 |

***onDraw，onTouchEvent，onMeasure，onSizeChanged，onLayout是被经常复写的方法***  

# View的位置Position

View的位置指两层，所在的X,Y坐标位置和View的尺寸大小。注意单位为像素
`The unit for location and dimensions is the pixel.`

# Size, padding and margins

padding 指的View的内容本身和View边界的距离
margin 指的View的边界和父容器的距离
# Layout

# Drawing

# Event Handling and Threading
View中基本的事件处理流程如下：

1. 事件发生后被分发到合适的View，View处理事件并发送提醒给所有的监听器
2. 如果事件处理的过程中View的边界需要调整，`requesetLayout()`方法将被调用
3. 同样的如果View的外观需要调整，`invalidate()`方法将被调用
4. 当`requestLayout()`或者`invalidate()`被调用，系统将会测量，重绘整个布局树。


# 焦点处理 (Foucus handling)

# 触摸模式(Touch Mode)

# 滚动(Scrolling)

# 标签(Tags)

# 主题(Themes)
# 属性(Properties)
# 动画(Animation)
# 安全(Security)

# 参考资料
1. [Android官方文档View](file:///D:/Android/sdk/docs/reference/android/view/View.html)
2. [Android应用坐标系统全面详解](http://blog.csdn.net/yanbober/article/details/50419117/)
3. [安卓自定义View基础：坐标系](http://android.jobbole.com/83276/)