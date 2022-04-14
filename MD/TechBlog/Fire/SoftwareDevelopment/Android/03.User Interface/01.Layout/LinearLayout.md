#　线性布局添加分割线：
新建drawable文件shape_ll_divider.xml
```
<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="@color/color_B3B3B3" />
    <size android:height="1dp" />
</shape>
```

需要用到分割线的地方：
```
android:divider="@drawable/shape_ll_divider"

android:showDividers="middle"
```

> showDividers取值有四:middle,end,beginning,noe.
    * middle 在每一项中间添加分割线
    * end 在整体的最后一项添加分割线
    * beginning 在整体的最上方添加分割线
    * none 无