
`This class represents the basic building block for user interface components. A View occupies a rectangular area on the screen and is responsible for drawing and event handling`

Android 中的坐标系有两类：
* 屏幕坐标系
* View的坐标系

**屏幕坐标系**  
屏幕坐标系以屏幕左上角为原点，向右为X轴增大方向，向下为Y轴增大方向。因此夹角的表示和数学坐标系中的夹角看起来略有不同但本质上是一致的。
![20170802170513.png](../../../../../Pictures\20170802\20170802170513.png)  

先了解下Android中屏幕的内容。
![20170802171534.png](../../../../../Pictures\20170802\20170802171534.png)  

**View的坐标系**  
View的坐标系是相对于父View的。



View中用于获取位置信息和X，Y相关的方法有下：

| 方法名 | 作用 |
|:--:|:--:|:--:|
| getScrollX() | |  
| getScrollY() | |
| getWidth() | |
| getHeight() | |
| getMeasuredWidth() | |
| getMeasureWidthAndState() | |
| getMeasureHeigtht() | |
| getMeasureHeightAndState() | |
| getRotationX() |  |
| getRotationY() |  |
| getScaleX() |  |
| getScaleY() |  |
| getPivotX() |  |
| getPivotY() |  |
| getTop() | |
| getBottom() | |
| getLeft() | |
| getRight() |  |
| getX() |  |
| getY() |  |
| getZ() |  |
| getTranslationX() |  |
| getTransaltionY() |  |
| getTranslationZ() |  |
| getPaddingXXX() |  |
| getLocationOnScreen() | |
| getLocationInWindow() |  |
| getMinimumHeight() |  |
| getMinimumWidth() |  |


# 参考资料
1. [Android官方文档View](file:///D:/Android/sdk/docs/reference/android/view/View.html)
2. [Android应用坐标系统全面详解](http://blog.csdn.net/yanbober/article/details/50419117/)
3. [安卓自定义View基础：坐标系](http://android.jobbole.com/83276/)
4. [android坐标](http://blog.csdn.net/lvxiangan/article/details/19971509)
5. [ANDROID VIEW BASICS: COORDINATES,MARGIN,PADDING,DIP,PX](https://laaptu.wordpress.com/tag/android-view-coordinate-systems/)