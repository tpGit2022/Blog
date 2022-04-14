> 基于Android Studio下的Android目录的讲解
> writed date:20170727
> update date:20170727

# res目录

| 目录 | 资源类型 |
|:--:|:--:|
| animator | 存放属性动画property animations资源 |
| anim | 存放补间动画tween animations资源 |
| color | 存放颜色选择器Color State List资源 |
| drawable | 存放位图(.png,.9.png,jpg,.gif)或者被编译成drawable对象的xml文件 |
| mipmap | 存放应用启动图标资源 |
| layout | 存放布局文件 |
| menu | 存放菜单文件 |
| raw | 可以存放任意文件 |
| values | 存放arrays.xml,colors.xml,dimens.xml,strings.xml,styles.xml,attrs.xml | 
| xml | 存放XML文件 |
| assets | 存放资源 |

## 各目录下可用的标签
* animator

| 标签 | 标签 | 标签 | 标签 |
|:--:|:--:|:--:|:--:|
| animator | objectAnimator | selector |  set| 

* anim

| 标签 | 标签 | 标签 |
|:----:|:----:|:----:|
| acclerateDecelerateInterpolator | accelerateInterpolator | alpha |
| anticipateInterpolator | anticipateOvershootInterpolator | bounceInterpolator |
| cycleInterpolator | decelerateInterpolator | gridLayoutAnimation |
| linearInterpolator | overshootInterpolator | pathInterpolator |
| rotate | scale | set | 
| translate | | |

* color
* drawable

| 标签 | 标签 | 标签 | 标签 |
|:--:|:--:|:--:|:--:|
| animated-rotate | animated-selector | animated-vector | animation-list | 
| bitmap | clip | color | inset | 
| layer-list | level-list | nine-patch | ripple |
| rotate | scale | selector | shape |
| transition | vector | | | 

* mipmap
* layout
* menu
* xml
# 参考资料
1. [](/sdk/docs/guide/topics/resources/providing-resources.html)