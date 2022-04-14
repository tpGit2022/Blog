利用SVG文件结合属性动画完成炫酷的动画效果。

1. drawable文件夹下新建SVG文件mul_start_drawable.xml  
```
<?xml version="1.0" encoding="utf-8"?>
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="500dp"
    android:height="500dp"
    android:viewportHeight="500.0"
    android:viewportWidth="500.0">
    <group
        android:scaleX="5.0"
        android:scaleY="5.0">
        <path
            android:name="path1"
            android:pathData="M 50.0,90.0 L 82.9193546357,27.2774101308 L 12.5993502926,35.8158045183 L 59.5726265715,88.837672697 L 76.5249063296,20.0595700732 L 10.2916450361,45.1785327898 L 68.5889268818,85.4182410261 L 68.5889268818,14.5817589739 L 10.2916450361,54.8214672102 L 76.5249063296,79.9404299268 L 59.5726265715,11.162327303 L 12.5993502926,64.1841954817 L 82.9193546357,72.7225898692 L 50.0,10.0 L 17.0806453643,72.7225898692 L 87.4006497074,64.1841954817 L 40.4273734285,11.162327303 L 23.4750936704,79.9404299268 L 89.7083549639,54.8214672102 L 31.4110731182,14.5817589739 L 31.4110731182,85.4182410261 L 89.7083549639,45.1785327898 L 23.4750936704,20.0595700732 L 40.4273734285,88.837672697 L 87.4006497074,35.8158045183 L 17.0806453643,27.2774101308 L 50.0,90.0Z"
            android:strokeColor="@color/colorAccent"
            android:strokeWidth="2"></path>
    </group>
</vector>
```

2. 在animator文件夹下新建属性动画mul_start_anim.xml
```
<?xml version="1.0" encoding="utf-8"?>
<set xmlns:android="http://schemas.android.com/apk/res/android">
    <objectAnimator
        android:duration="5000"
        android:propertyName="trimPathStart"
        android:repeatMode="restart"
        android:valueFrom="1"
        android:valueTo="0" />
    <objectAnimator
        android:duration="5000"
        android:propertyName="strokeColor"
        android:repeatCount="infinite"
        android:repeatMode="restart"
        android:valueFrom="@color/colorAccent"
        android:valueTo="@color/colorPrimaryDark" />
</set>
```

3. 关联SVG文件和属性动画，drawable文件夹下新建draw_combine.xml文件。
```
<?xml version="1.0" encoding="utf-8"?>
<animated-vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:drawable="@drawable/mul_start_drawable"
    >
    <target
        android:animation="@animator/mul_start_anim"
        android:name="start"/>
</animated-vector>
```

> drawable指定要进行动画操作的drawable对象，animation指要进行的动画，name指drawable中name为start的path。`android:animation="@animator/mul_start_anim"`,Android Studio不会自动提示需要自己手动不全，且animated-vector会标红提示。  
> ![20170803113556.png](../../../../Pictures\20170803\20170803113556.png)  

4. 在布局文件中引用draw_combine.xml.
```
<ImageView
        android:id="@+id/iv_ivsvg"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        app:srcCompat="@drawable/draw_combine"
        />
```

> 引入app命名空间，修改android:src为app:srcCompat，同样scrCompat，AS不会自动提示，需要手动输入,srcCompat指向关联SVG文件和属性动画的draw_combine文件。

5. 在代码中启动动画。
```
        ImageView iv_ivsvg= (ImageView) findViewById(R.id.iv_ivsvg);
        Drawable drawable=iv_ivsvg.getDrawable();
        if(drawable instanceof  Animatable){
            ((Animatable) drawable).start();    
        }
```

***tips:***
* 常见的错误空指针异常。
`java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.Class java.lang.Object.getClass()' on a null object reference`

排除该错误确认两点：
1. 保证imageview引用的是正确的drawable，即连接drawable和动画的drawable文件而不是单纯的drawable文件。
2. 确保`draw_combine.xml`文件中target节点的name属性指向正确，其值必须与`mul_start_drawable.xml `文件中name属性的值一致。