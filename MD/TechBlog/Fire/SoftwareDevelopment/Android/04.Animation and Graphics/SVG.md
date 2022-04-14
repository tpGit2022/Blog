SVG 矢量图相较于传统的png,jpg等图片资源不会有失真的问题，在不同分辨率下一样清晰  
SVG在Android上面主要的坑在于兼容性上面，在Android5.0以上和以下，需要做出不同的处理。

为了尽可能的少踩坑，使用最新的support library，build tool。

Android 5.0以上svg资源直接使用即可，5.0以下需要做好兼容处理。
* `build.gradle`开启svg支持android-defaultConfig节点添加
`vectorDrawables.useSupportLibrary = true`
* 添加static静态代码块
```
static {
    AppCompatDelegate.setCompatVectorFromResourcesEnabled(true);
}
```

上述代码用于解决使用了`selector`等包含了矢量图资源的drawable在Android5.0以下发生报错的问题。

之后布局文件中引用时添加app命名空间。使用`app:compatSrc`代替`android:src`.

drawable-anydpi-v21

当然直接的SVG文件Android是无法引用的，需要经过Android Studio的Vector Asset工具将SVG文件转化为xml，最后再控件中以drawable对象的方式被引用。

过于复杂的svg文件在Android设备上不一定可以正常显示，也许5.0以上正常5.0以下就显示有问题，曾在5.0以下得到以下警告，在5.0以下svg显示不正常。

```
W/PathParser: Points are too far apart 26.026992567721024
```
打印这段警告的源码位于`android/util/PathParser.java`
源码位于`https://android.googlesource.com/platform/frameworks/base/+/17e64ffd852f8fe23b8e2e2ff1b62ee742af17a6/core/java/android/util/PathParser.java#417`

看情况是绘制圆弧是当某种因子太小时等比例扩大x，y再绘制圆弧。

调整svg的信息密度后5.0以下显示也正常了。


引用svg的drawable的imageview需要使用`app:srcCompat` 替代 `android:src`


目录 drawable，anim，animator。
anim目录中的标签:

| 标签 | 标签 | 标签 |
|:----:|:----:|:----:|
| acclerateDecelerateInterpolator | accelerateInterpolator | alpha |
| anticipateInterpolator | anticipateOvershootInterpolator | bounceInterpolator |
| cycleInterpolator | decelerateInterpolator | gridLayoutAnimation |
| linearInterpolator | overshootInterpolator | pathInterpolator |
| rotate | scale | set | 
| translate | | |

animator中的标签:

| 标签 | 标签 | 标签 | 标签 |
|:--:|:--:|:--:|:--:|
| animator | objectAnimator | selector |  set| 

drawable目录中的标签：

| 标签 | 标签 | 标签 | 标签 |
|:--:|:--:|:--:|:--:|
| animated-rotate | animated-selector | animated-vector | animation-list | 
| bitmap | clip | color | inset | 
| layer-list | level-list | nine-patch | ripple |
| rotate | scale | selector | shape |
| transition | vector | | | 


问题之一，如何在高版本上优先使用svg文件。

# 参考资料
1. [ Android Vector曲折的兼容之路](http://blog.csdn.net/eclipsexys/article/details/51838119)
2. [Using android vector Drawables on pre Lollipop crash](https://stackoverflow.com/questions/36867298/using-android-vector-drawables-on-pre-lollipop-crash)
3. [Android使用SVG小结](https://www.jianshu.com/p/c6614fb502c4)
4. [Google Docs - SVG](https://developer.android.com/guide/topics/graphics/vector-drawable-resources)
5. [使用androidvector在前棒棒糖崩溃的Drawables](http://androidcookie.com/androidvectordrawables.html)
6. [Android 矢量图支持分析](https://ayaseruri.net/2017/06/24/Android-矢量图支持分析.html)
7. [AppCompat — Age of the vectors](https://medium.com/@chrisbanes/appcompat-v23-2-age-of-the-vectors-91cbafa87c88)
8. [Android vector 标签 pathData 详解 - 简书](https://www.jianshu.com/p/a3cb1e23c2c4)
9. [Android矢量图VectorDrawable](https://www.jianshu.com/p/04cda03a6b71)
10. [美工死不瞑目系列之SVG推锅技巧！](https://www.jianshu.com/p/ad9b7382aecb)
11. [Android vector 标签 pathData 详解](https://www.jianshu.com/p/a3cb1e23c2c4)