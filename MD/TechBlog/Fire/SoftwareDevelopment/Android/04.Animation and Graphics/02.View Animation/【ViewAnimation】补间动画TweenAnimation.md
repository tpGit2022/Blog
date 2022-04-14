[TOC]

# 动画类型
补间动画(Tween Animation)提供四种操作：旋转(rotate),淡入淡出(fade),位移(move),拉伸(stretch)。

四种操作对应的java类和xml中的属性节点关系如下表格：

| 操作 | 类名 | 节点名 |
|:--:|:--:|:--:|
| 旋转 | RotateAnimation | rotate |
| 淡入淡出 | AlphaAnimation | alpha |
| 位移 | TranslateAnimation | translate |
| 拉伸 | ScaleAnimation | scale |

## 旋转动画

实现一个旋转动画有两种实现方式：1.xml实现动画效果，代码引用。2,完全代码实现。

### xml实现旋转动画
xml中可用于旋转动画的属性如下：

| 属性名 | 用途 | 备注 |
|:--:|:--:|:--:|
| android:fromDegrees | 旋转开始的角度，其值为角度制  | 数据类型float |
| android:toDegress | 旋转的终止角度 | 数据类型float |
| android:pivotX | 旋转中心的X轴坐标 | 数据类型为float或者百分比 |
| android:pivotY | 旋转中心的Y轴坐标 | 数据类型为float或者百分比 |
| android:duration | 动画持续的时间 | 其单位为毫秒ms，3000代表3秒 |

**旋转中心的说明**  
**android:pivotX** 
官方原文：  
***Float or percentage. The X coordinate of the center of rotation. Expressed either: in pixels relative to the object's left edge (such as "5"), in percentage relative to the object's left edge (such as "5%"), or in percentage relative to the parent container's left edge (such as "5%p").***
翻译过来大致是：
旋转起点X坐标（数值、百分数、百分数p，譬如5表示以当前View左上角坐标加5px为初始点、5%表示以当前View的左上角加上当前View宽高的5%做为初始点、5%p表示以当前View的左上角加上父控件宽高的5%p做为初始点）
例如：让一个80\*80dp的TextView，绕其3s内中心旋转360度的动画文件tween_anim_rotate.xml如下：
```
<?xml version="1.0" encoding="utf-8"?>
<rotate xmlns:android="http://schemas.android.com/apk/res/android"
    android:fromDegrees="0"
    android:pivotX="120"
    android:pivotY="120"
    android:duration="3000"
    android:toDegrees="360">
</rotate>
```
假定TextView的左上角的坐标为(vx,vy)，旋转中心应为(vx+40dp,vy+40dp)
pivotX其值为120而非40的原因在于布局文件中的pivotX是px而非dp，在不同设备中1dp表示的px值并非一致，所以在xml中pivotX更多用到的是百分比形式。
* 以自身为百分比的形式,旋转中心应为(vx+40dp/80dp\*100%,vy+40dp/80dp\*100%)
```
android:pivotX="50%"
android:pivotY="50%"
```
* 以父控件为百分比的形式(假定父控件为240\*240dp,此时旋转中心为(vx+40dp/240dp\*100%,vy+40dp/240dp\*100%))
```
android:pivotX="16.6%p"
android:pivotY="16.6%p"
```

让控件执行上面定义的旋转动画的代码如下：
```
//初始化动画实例
 Animation animation = AnimationUtils.loadAnimation(this, R.anim.tween_anim_rotate);
//控件执行动画效果
xxx.startAnimation(animation);
```
### 代码实现旋转动画
要代码实现旋转动画需要借助RotateAnimation这个类，该类有四个构造方法。

* `RotateAnimation(Context context, AttributeSet attrs)`
* `RotateAnimation(float fromDegrees, float toDegrees)`
* `RotateAnimation(float fromDegrees, float toDegrees, float pivotX, float pivotY)`
* `RotateAnimation(float fromDegrees, float toDegrees, int pivotXType, float pivotXValue,int pivotYType, float pivotYValue)`

需要关注的是后三个构造方法。稍微说下最后一个方法。
`pivotXType` 指的旋转中心X轴坐标值的类型和xml文件中的具体指，百分比相对应，其值为`Animation.ABSOLUTE, Animation.RELATIVE_TO_SELF,Animation.RELATIVE_TO_PARENT` 三者之一。

同样实现一个80\*80dp的TextView，绕其3s内中心旋转360度的动画代码如下：

```
        float piovX=DimensionUtils.dip2px(this,40);
        float piovY=DimensionUtils.dip2px(this,40);
        RotateAnimation rotateAnimation=new RotateAnimation(0,360,piovX,piovY);
        rotateAnimation.setDuration(5000);
        tv_tween.startAnimation(rotateAnimation);
```
或者
```
        //以View本身作为基准
        float fractionX=40f/80;
        float fractionY=40f/80;
        RotateAnimation rotateAnimation=new RotateAnimation(0,360,Animation.RELATIVE_TO_SELF,fractionX,Animation.RELATIVE_TO_SELF,fractionY);
        rotateAnimation.setDuration(5000);
        tv_tween.startAnimation(rotateAnimation);
```
再或者(以父控件240\*240dp，计算)
```
        //以View的父控件作为基准
        float fractionX=40f/240;
        float fractionY=40f/240;
        RotateAnimation rotateAnimation=new RotateAnimation(0,360,Animation.RELATIVE_TO_PARENT,fractionX,Animation.RELATIVE_TO_PARENT,fractionY);
        rotateAnimation.setDuration(3000);
        tv_tween.startAnimation(rotateAnimation);
```
## 淡入淡出动画
淡入淡出动画借助于透明度来实现，同样有两种方式：xml和代码实现。
### xml实现淡入淡出动画
透明度动画xml中可以用到的属性。

| 属性名称 | 用途 | 备注 |
|:--:|:---:|:--:|
| android:fromAlpha | 动画开始时的透明度 | 类型为float，0.0代表透明，1.0代表完全不透明 |
| android:toAlpha | 动画结束时的透明度 | 类型为float，0.0代表透明，1.0代表完全不透明 |
| android:duration | 动画持续的时间 | 其单位为毫秒ms，3000代表3秒 |

动画实现TextView 3s内有可见变为不可见。透明度动画文件anim.tween_anim_alpha.xml如下：
```
<?xml version="1.0" encoding="utf-8"?>
<alpha xmlns:android="http://schemas.android.com/apk/res/android"
    android:duration="3000"
    android:fromAlpha="1"
    android:toAlpha="0">
</alpha>
```

代码中载入动画：
```
 private void loadAlphaAnimationFromXml(){
        Animation animation=AnimationUtils.loadAnimation(this,R.anim.tween_anim_alpha);
        xxxx.startAnimation(animation);
    }
```
### 代码实现淡入淡出动画
代码实现透明度动画需借助AlphaAnimation类支持，该类有两个构造方法：

* `AlphaAnimation(Context context, AttributeSet attrs)`
* `AlphaAnimation(float fromAlpha, float toAlpha)`

同样代码实现TextView 3s内有可见变为不可见的透明度动画如下：
```
    private void loadAlphaAnimationByCode(){
        AlphaAnimation alphaAnimation=new AlphaAnimation(1.0f,0f);
        alphaAnimation.setDuration(3000);
        tv_tween.startAnimation(alphaAnimation);
    }
```
## 位移动画
位移动画是发生于垂直或者水平的移动。位移动画需要两个点：开始点和结束点。
也就是需要四个坐标参数：两点的X和Y轴的坐标。与旋转动画的pioxtX的值类似，位移动画的坐标值也支持百分比形式，同样实现位移动画存在两种方式：1.xml实现 2.代码实现。同样的百分比形式下偏移的基准点是基于当前View的左上角(x0,y0)。
### xml实现位移动画
xml中可以用到的属性名。

| 属性名 | 作用 | 备注 |
|:---:|:---:|:---:|
| android:fromXDelta | 位移开始点的X轴坐标 | 其值为float或者百分比 |
| android:fromYDelta | 位移开始点的Y轴坐标 | 其值为float或者百分比 |
| android:toXDelta | 位移结束点的X轴坐标 | 其值为float或者百分比 |
| android:toYDelta | 位移结束点的Y轴坐标 | 其值为float或者百分比 |

正方形的TextView沿其对角线方向滑动一个对角线的距离的动画文件tween_anim_translate.xml。
```
<?xml version="1.0" encoding="utf-8"?>
<translate xmlns:android="http://schemas.android.com/apk/res/android"
    android:fromXDelta="0%"
    android:fromYDelta="0%"
    android:toXDelta="100%"
    android:toYDelta="100%"
    >
</translate>
```

代码中载入动画。
```
    private void loadTranslateAnimFromXml(){
        Animation animation=AnimationUtils.loadAnimation(this,R.anim.tween_anim_translate);
        animation.setDuration(3000);
        tv_tween.startAnimation(animation);
    }
```

### 代码实现位移动画
代码实现位移动画需要借助TranslateAnimation类的支持，该类有3个构造方法：

* `TranslateAnimation(Context context, AttributeSet attrs)`
* `TranslateAnimation(float fromXDelta, float toXDelta, float fromYDelta, float toYDelta)`
* `TranslateAnimation(int fromXType, float fromXValue, int toXType, float toXValue,int fromYType, float fromYValue, int toYType, float toYValue)`

> 注意 参数的位置。从左至右是x0,x1,y0,y1

代码实现同样效果：
```
    private void loadTranslateAnimByCode(){
        float fractionX0=0f;
        float fractionY0=0f;
        float fractionX1=1f;
        float fractionY1=1f;
        TranslateAnimation translateAnimation=new TranslateAnimation(Animation.RELATIVE_TO_SELF,fractionX0,
                Animation.RELATIVE_TO_SELF,fractionX1,Animation.RELATIVE_TO_SELF,fractionY0,
                Animation.RELATIVE_TO_SELF,fractionY1);
        translateAnimation.setDuration(3000);
        tv_tween.startAnimation(translateAnimation);
    }
```
## 拉伸动画
拉伸动画scale是对控件长宽的处理，拉伸动画需要一个中心点，直观上看拉伸动画就是各点到中心的距离发生了变化。实现一个拉伸动画有两种方法 1. xml实现 2.纯代码实现 。
### xml实现拉伸动画
可用于xml的拉伸动画的属性值如下：

| 属性名 | 用途 | 备注 |
|:---:|:--:|:--:|
| android:fromXScale | 动画开始时x轴的缩放比例 | 其值为float,fraction,dimension即浮点型，百分比和尺寸，为1.0时代表无缩放 |
| android:toXScale | 动画结束时x轴的缩放比例 | 其值为float,fraction,dimension即浮点型，百分比和尺寸，为1.0时代表无缩放 |
| android:fromYScale | 动画开始时y轴的缩放比例 | 其值为float,fraction,dimension即浮点型，百分比和尺寸，为1.0时代表无缩放 |
| android:toYScale | 动画结束时y轴的缩放比例 | 其值为float,fraction,dimension即浮点型，百分比和尺寸，为1.0时代表无缩放 |
| android:pivotX | 缩放中心的x轴坐标 | 其值为浮点型或者百分比 |
| android:pivotY | 缩放中心y轴的坐标 | 其值为浮点型或者百分比 |

实现一个TextView以其中心缩放一半的拉伸动画文件tween_anim_scale.xml文件如下：
```
<?xml version="1.0" encoding="utf-8"?>
<scale xmlns:android="http://schemas.android.com/apk/res/android"
    android:fromXScale="1"
    android:toXScale="0.5"
    android:fromYScale="1"
    android:toYScale="0.5"
    android:pivotX="50%"
    android:pivotY="50%"
    >
</scale>
```
代码中引用：
```
 private void loadScaleAnimFromXml(){
        Animation animation=AnimationUtils.loadAnimation(this,R.anim.tween_anim_scale);
        animation.setDuration(5000);
        tv_tween.startAnimation(animation);
    }
```

### 代码实现拉伸动画 

代码实现拉伸动画需要借助ScaleAnimation类的支持，该类有四个构造方法：

* `ScaleAnimation(Context context, AttributeSet attrs)`
* `ScaleAnimation(float fromX, float toX, float fromY, float toY)`
* `ScaleAnimation(float fromX, float toX, float fromY, float toY,float pivotX, float pivotY)`
* `ScaleAnimation(float fromX, float toX, float fromY, float toY,int pivotXType, float pivotXValue, int pivotYType, float pivotYValue)`

代码实现同样效果：
```
    private void loadScaleAnimByCode(){
        float fractionPVX=0.5f;
        float fractionPVY=0.5f;
        ScaleAnimation scaleAnimation=new ScaleAnimation(1f,0.5f,1f,0.5f,
                Animation.RELATIVE_TO_SELF,fractionPVX,Animation.RELATIVE_TO_SELF,fractionPVY);
        scaleAnimation.setDuration(5000);
        tv_tween.startAnimation(scaleAnimation);
    }
```
# 动画集合
动画集合用于完成一组如旋转，拉伸，位移动画的组合。java类是AnimationSet，xml文件中对应的节点是`set`。动画集合可以嵌套动画集合，即set节点里面可以有其他的set节点。
xml文件中set节点常会用到的两个属性

* ***android:interpolator*** 动画的插值器
* ***android:shareInterpolator*** set的子节点是否共用一个插值器
例如实现一个TextView以中心缩放的同时旋转，动画的文件tween_anim_set.xml可以这样写：
```
<?xml version="1.0" encoding="utf-8"?>
<set xmlns:android="http://schemas.android.com/apk/res/android"
    android:interpolator="@android:anim/accelerate_decelerate_interpolator"
    android:shareInterpolator="true">
    <scale
        android:fromXScale="1"
        android:fromYScale="1"
        android:pivotX="50%"
        android:pivotY="50%"
        android:toXScale="0.5"
        android:toYScale="0.5"></scale>

    <rotate
        android:fromDegrees="0"
        android:pivotX="50%"
        android:pivotY="50%"
        android:toDegrees="360"></rotate>
</set>
```
代码中引用：
```
 private void loadAnimSetFromXml(){
        Animation animation=AnimationUtils.loadAnimation(this,R.anim.tween_anim_set);
        animation.setDuration(3000);
        tv_tween.startAnimation(animation);
    }
```

完全代码实现：
```
    private void loadAnimSetByCode(){
        //传递的true就是布局文件中设置的shareInterpolator属性
        AnimationSet animationSet=new AnimationSet(true);
        float fractionPVX=0.5f;
        float fractionPVY=0.5f;
        ScaleAnimation scaleAnimation=new ScaleAnimation(1f,0.5f,1f,0.5f,
                Animation.RELATIVE_TO_SELF,fractionPVX,Animation.RELATIVE_TO_SELF,fractionPVY);
        float fractionX=40f/80;
        float fractionY=40f/80;
        RotateAnimation rotateAnimation=new RotateAnimation(0,360,Animation.RELATIVE_TO_SELF,fractionX,Animation.RELATIVE_TO_SELF,fractionY);
        animationSet.addAnimation(scaleAnimation);
        animationSet.addAnimation(rotateAnimation);
        animationSet.setDuration(3000);
        tv_tween.startAnimation(animationSet);
    }
```
补间动画xml文件的写法。
补间动画的资源文件存放于res/anim文件夹下。
```
<?xml version="1.0" encoding="utf-8"?>
<set xmlns:android="http://schemas.android.com/apk/res/android"
    android:duration="integer"
    android:fillAfter="boolean"
    android:repeatMode="enum[restart,reverse]"
    android:fillBefore="boolean"
    android:shareInterpolator="boolean"
    android:startOffset="integer">
    <scale
        android:pivotX="float,fraction"
        android:pivotY="float,fraction"
        android:fromXScale="float,fraction,dimension"
        android:fromYScale="float,fraction,dimension"
        android:toXScale="float,fraction,dimension"
        android:toYScale="float,fraction,dimension"
        />
    <alpha
        android:fromAlpha="float"
        android:toAlpha="float"
        />
    <rotate
        android:pivotY="float,fraction"
        android:fromDegrees="float"
        android:pivotX="float,fraction"
        android:toDegrees="float"
        />
    <translate
        android:fromXDelta="float,fraction"
        android:fromYDelta="float,fraction"
        android:toXDelta="float,fraction"
        android:toYDelta="float,fraction"
        />
</set>
```


# 总结

# 参考资料
