styles.xml 位于res/values目录之下。style是一串属性的集合，用于描述view，activity或者整个app。

> A style is a collection of properties that specify the look and format for a View or window

styles.xml的格式如下：
```
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <style name="style_name" parent="parent_style_name">
        <item
            name="propertname"
        >style_name
        </item>
    </style>
</resources>
```

例如定义一个TextView背景为蓝色，字体大小为16sp，字颜色为红色的style文件为：
```
<resources>
    <style name="TextViewTemplate">
        <item name="android:background">@android:color/holo_blue_light</item>
        <item name="android:textSize">16sp</item>
        <item name="android:textColor">@android:color/holo_red_light</item>
    </style>
</resources>
```
某个TextView在布局中通过style属性对其进行应用。
```
<TextView
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    style="@style/TextViewTemplate"
/>
```
# 节点说明
## resources
没什么好说的，`<resources>`一向是res/values文件夹下的根节点。没有可用属性
## style
`<style>`节点有两个可用的属性name和parent。其中name属性是必须的，其值为string类型，name被当初ID被外部资源当style引用。parent为可选属性，用于指明该style继承至那个style。parent节点更多的用于使用Android系统资源，如果父style是自定义的style，有种更简单的方法\.分割，如下的例子定义了新的style名为Child的属性，该属性继承至TextViewTemplate。
```
<style name="TextViewTemplate.Child" >
        <item name="android:background">@android:color/holo_red_light</item>
        <item name="android:textSize">16sp</item>
        <item name="android:textColor">@android:color/holo_red_light</item>
    </style>
```

## item
`<item>`必须作为`<style>`子节点，`<item>`的属性name指向view，activity或者application的某一属性。`<item>`和`</item>`之间的内容决定该属性具体的值。

***注意***  
子style的同名属性会覆盖父style的同名属性。