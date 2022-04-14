[TOC]

帧动画Frame Animation也称Drawable Animation。简单来讲实现的是幻灯片的效果，是图片之间的切换 。
Java类是AnimationDrawable，xml中的节点名是animation-list。

> 帧动画的xml资源存放于drawable文件夹下而非anim文件夹。

drawable下新建frame_anim.xml
```
<?xml version="1.0" encoding="utf-8"?>
<animation-list xmlns:android="http://schemas.android.com/apk/res/android"
    android:oneshot="true">
    <item
        android:drawable="@drawable/draw_combine"
        android:duration="1000"></item>
    <item
        android:drawable="@drawable/anim_vetor"
        android:duration="2000"></item>
</animation-list>
```
代码中应用:
```
 AnimationDrawable animationDrawable= (AnimationDrawable) ivFrame.getBackground();
 animationDrawable.start();
```

纯代码实现：
```
 private void loadFrameAnimByCode(){
        Drawable frame1=getResources().getDrawable(R.drawable.draw_combine);
        Drawable frame2=getResources().getDrawable(R.drawable.anim_vetor);
        AnimationDrawable animationDrawable=new AnimationDrawable();
        animationDrawable.addFrame(frame1,1000);
        animationDrawable.addFrame(frame2,1000);
        ivFrame.setImageDrawable(animationDrawable);
        animationDrawable.start();
    }
```