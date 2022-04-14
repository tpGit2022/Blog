BottomSheet的使用.

BottomSheet即从app的底部弹出的遮罩层。

1. BottomSheetBehavior
2. BottomSheetDialog
3. BottomSheetDialogFragment

# BottomSheetBehavior
***An interaction behavior plugin for a child view of CoordinatorLayout to make it work as a bottom sheet.***  
BottomSheetBehavior常和协调布局CoordinatorLayout一起使用(为了解决滑动嵌套问题也经常和NestedScrollView连用)。
```
<?xml version="1.0" encoding="utf-8"?>
<android.support.design.widget.CoordinatorLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:fitsSystemWindows="true"
    android:orientation="vertical"
    tools:context=".bottomsheet.BottomSheetActivity">
    ...
    <android.support.v4.widget.NestedScrollView
        android:id="@+id/scroll"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        app:behavior_hideable="true"
        app:behavior_peekHeight="40dp"
        app:layout_behavior="android.support.design.widget.BottomSheetBehavior">

        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="vertical">

            <TextView
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:background="@color/colorPrimary"
                android:padding="50dp"
                android:text="@string/app_name" />
        </LinearLayout>
    </android.support.v4.widget.NestedScrollView>
</android.support.design.widget.CoordinatorLayout>
```
常用的XML中的属性：
* app:behavior_hideable    决定BottomSheet是否可以被隐藏，默认为false
* app:behavior_peekHeight  BottomSheet处于关闭状态时的高度,默认值为0
* app:layout_behavior      指定BottomSheet一般其值为android.support.design.widget.BottomSheetBehavior
BottomSheet的几种状态。

> 注意：BottomSheet的关闭不等于不可见。peekHeight的高度决定了关闭状态的BottomSheet的高度。 

| 状态值名称 | 状态值数值 |状态说明 |
|:---:|:---:|:---:|
| STATE_DRAGGING | 1 | 正在绘制 |
|  STATE_SETTLING |
| STATE_EXPANDED |
| STATE_COLLAPSED |
| STATE_HIDDEN |

STATE_HIDDEN: 隐藏状态。默认是false，可通过app:behavior_hideable属性设置。
STATE_COLLAPSED: 折叠关闭状态。可通过app:behavior_peekHeight来设置显示的高度,peekHeight默认是0。
STATE_DRAGGING: 被拖拽状态
STATE_SETTLING: 拖拽松开之后到达终点位置（collapsed or expanded）前的状态。
STATE_EXPANDED: 完全展开的状态。
>design24.2.1的BottomSheets和23.2.0的BottomSheet有很大的区别,design23.2.0的包中如果你使用了BottomSheet,可以在屏幕外任何位置上拉即可拉出来布局,在24.2.1中没有了这个效果。 

# BottomSheetDialog
***Base class for Dialogs styled as a bottom sheet.***  
dialog的布局文件可以不被协调布局CoordinatorLayout所包裹。
# BottomSheetDialogFragment
***Modal bottom sheet. This is a version of DialogFragment that shows a bottom sheet using BottomSheetDialog instead of a floating dialog.***  

BottomSheetDialogFragment的源码如下：
```
public class BottomSheetDialogFragment extends AppCompatDialogFragment {

    @Override
    public Dialog onCreateDialog(Bundle savedInstanceState) {
        return new BottomSheetDialog(getContext(), getTheme());
    }

}
```

从中可以看到

