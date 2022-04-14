[TOC]

当 Android 原生控件无法满足时就需要用到自定义View，自定义View分类上有：

自定义View

需要关注的方法：

读取自定义属性，margin，padding 继续保持有效状态，设置的background(drawable文件)依旧有效

ViewGrup 的流程 和 View 的流程的差异？

绘制的顺序


| Category | 	Methods | 	Description
|:--|:--|:--|
| 创建	| 构造方法	| 构造方法存在多个，可读取xml布局中配置的参数
| | onFinishInflate()| 从布局文件中完成view的创建后调用 | 
| 布局 |	onMeasure(int, int) |	测量view和子孙View的大小. |
| | onLayout(boolean, int, int, int, int) | 决定view和子孙view放置的位置. |
| | onSizeChanged(int, int, int, int) |	view的尺寸有变化被调用 |
| 绘制 |	onDraw(android.graphics.Canvas) | 绘制View的内容 |
| 事件处理 | onKeyDown(int, android.view.KeyEvent) | 硬件按钮被按下时触发
| | onKeyUp(int, android.view.KeyEvent)	| 硬件按钮弹起时触发
| | onTrackballEvent(android.view.MotionEvent) | 轨迹球事件回调 |
| | onTouchEvent(android.view.MotionEvent) | 屏幕点击事件回调 |
| 焦点 | 	onFocusChanged(boolean, int, android.graphics.Rect)	| 获取和失去焦点时被调用 |
| | onWindowFocusChanged(boolean) | Called when the window containing the view gains or loses focus.
| Attaching	 | onAttachedToWindow() | 	Called when the view is attached to a window.
| | onDetachedFromWindow() |	Called when the view is detached from its window.
| | onWindowVisibilityChanged(int) |	Called when the visibility of the window containing the view has changed.


需要着重关注的是 onMeasure,onLayout,onDraw 三个方法


# 构造

自定义 View 时免不了复写构造方法，一段常见的代码如下：

```
    public HalfTextView(Context context) {
        super(context,null);
    }

    public HalfTextView(Context context, @Nullable AttributeSet attrs) {
        super(context, attrs);
        paint = new Paint(Paint.ANTI_ALIAS_FLAG);
        TypedArray typedArray = getContext().obtainStyledAttributes(attrs, R.styleable.HalfTextView);
        leftColor = typedArray.getColor(R.styleable.HalfTextView_leftColor, Color.parseColor("#363636"));
        rightColor = typedArray.getColor(R.styleable.HalfTextView_rightColor, Color.parseColor("#FF383B"));
        gradient = typedArray.getFloat(R.styleable.HalfTextView_gradient, 30F);

        xColor = Color.parseColor("#FFB154");
        yColor = Color.parseColor("#FFB154");
        pathLeft = new Path();

        pathRight = new Path();
    }
```

第二个构造方法中从 `res/values/attrs.xml` 中读取初始化配置，`res/values/attrs.xml` 的内容如下:

```
    <declare-styleable name="HalfTextView">
        <attr name="leftColor" format="color"/>
        <attr name="rightColor" format="color"/>
        <attr name="gradient" format="float"/>
    </declare-styleable>
```

从 `android.view.View.draw(Canvas canvas)` 源码中可以看出来绘制流程

```
/**
     * Manually render this view (and all of its children) to the given Canvas.
     * The view must have already done a full layout before this function is
     * called.  When implementing a view, implement
     * {@link #onDraw(android.graphics.Canvas)} instead of overriding this method.
     * If you do need to override this method, call the superclass version.
     *
     * @param canvas The Canvas to which the View is rendered.
     */
    @CallSuper
    public void draw(Canvas canvas) {
         /*
         * Draw traversal performs several drawing steps which must be executed
         * in the appropriate order:
         *
         *      1. Draw the background
         *      2. If necessary, save the canvas' layers to prepare for fading
         *      3. Draw view's content
         *      4. Draw children
         *      5. If necessary, draw the fading edges and restore layers
         *      6. Draw decorations (scrollbars for instance)
         */
         ....
    }
```

自定义View主要的几个点：

1. View的绘制
2. View的事件分发处理
3. View的动效


自定义 View 的绘制中需要注意 dp，pixel 以及角度和弧度等单位，一般而言 View 的方法多以pixel 作为度量单位，角度和弧度需要根据实际函数的情况来确定。


# 参考资料
1. [Google-Android-View-Docs](https://developer.android.google.cn/reference/android/view/View)