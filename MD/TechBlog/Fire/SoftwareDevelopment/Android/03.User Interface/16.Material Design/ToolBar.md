Toolbar配合使用 

基本写法：
```
<android.support.v7.widget.Toolbar
        android:id="@+id/toolbar"
        android:layout_width="match_parent"
        android:layout_height="?android:actionBarSize"
        android:fitsSystemWindows="true"
        >
</android.support.v7.widget.Toolbar>
```

实现全屏的主题的style样式:
```
<style name="AppBaseTheme" parent="Theme.AppCompat.Light.DarkActionBar">
        <item name="colorPrimary">@color/colorPrimary</item>
        <item name="colorPrimaryDark">@color/colorPrimaryDark</item>
        <item name="colorAccent">@color/colorAccent</item>
    </style>
    <!-- Application theme. -->
    <style name="AppTheme" parent="AppBaseTheme">
    </style>
    <!-- NoActionBar theme. -->
    <style name="AppTheme.NoActionBar">
        <item name="windowActionBar">false</item>
        <item name="windowNoTitle">true</item>
    </style>
    <!-- Fullscreen theme. -->
    <style name="AppTheme.FullScreen">
        <item name="windowNoTitle">true</item>
        <item name="windowActionBar">false</item>
        <item name="android:windowFullscreen">true</item>
        <item name="android:windowContentOverlay">@null</item>
        <item name="android:windowIsTranslucent">false</item>
    </style>
```

# 常见问题
1. 使用Toolbar或者ActionBar左右两侧或者一侧出现黑色空白区域的问题。
解决方案：出现空白区域是由于自带的ActionBar或者Toolbar的样式导致的，重写属性即可。
ActionBar的写法。
**注意** ：是`actionBarStyle`不是`actionBarTheme`
```
<!--解决使用v7包下的ActionBar左右侧边出现黑色空白的问题-->
    <style name="actionbarstyle" parent="Widget.AppCompat.ActionBar">
        <item name="contentInsetStart">0dp</item>
        <item name="contentInsetEnd">0dp</item>
    </style>
//然后再定义的主题中引用
 <style name="AppCompatTheme" parent="Theme.AppCompat.Light.DarkActionBar">
        <item name="actionBarStyle">@style/actionbarstyle</item>
    </style>
```
Toolbar的写法
```
<style name="toolbarstyle" parent="Widget.AppCompat.Toolbar">
        <item name="contentInsetStart">0dp</item>
        <item name="contentInsetEnd">0dp</item>
    </style>
//主题中引用
 <style name="AppCompatTheme" parent="Theme.AppCompat.Light.DarkActionBar">
        <item name="toolbarStyle">@style/toolbarstyle</item>
    </style>
```

# 参考资料
1. [使用appcompat_v7，定义activity全屏或无标题栏](http://blog.csdn.net/lpforever/article/details/40507143)
2. [](http://blog.csdn.net/l331258747/article/details/52910247)


