> 用作TextView控件的使用总结

***TextView***
> update 2016/12/26

1. 为TextView的上下左右设置图片。  
设置图片的
  1. 在xml文件中为上下左右设置图片。个人不太懂 `android:drawableStart`和`android:drawableLeft`以及`android:drawableEnd`和`android:drawableRight`之间的区别，两者的使用实际效果显示一致。`drawableEnd`的官方解释 *The drawable to be drawn to the end of the text. [color, reference]* ，而`drawableRight`的官方解释 *The drawable to be drawn to the right of the text. [color, reference]*。当两者同时使用最终效果取决于后面定义的属性。比如同时使用`drawableStart`和`drawableLeft`,前者位置靠前后者靠后，则最终效果由`drawableLeft`决定。drawableXXX引用的可以是一个drawable下面的selector文件用于指定不同状态下选择展示的内容。`drawablePadding`属性决定图片和text内容的距离。
  ```
    <TextView
        android:id="@+id/tv_demo"
        android:layout_width="match_parent"
        android:layout_height="300dp"
        android:background="@color/color_C7EDCC"
        android:padding="10dp"
        android:layout_margin="5dp"
        android:textColor="@color/color_6AB344"
        android:drawableLeft="@drawable/ic_launcher"
        android:drawableStart="@drawable/qq"
        android:drawableTop="@drawable/ic_launcher"
        android:drawableBottom="@drawable/qq"
        android:drawableEnd="@drawable/qq"
        android:drawablePadding="2dp"
        android:drawableRight="@drawable/qq"
        android:text="@string/content" />
  ```
   效果如下图:  
     ![20161226161821.png](../../../../../Pictures\20161226\20161226161821.png)

   2. 代码实现。通过TextView的setCompoundXXX一系列方法实现。注意查看该系列方法的要求同时注意该方法的对版本的要求，比如`setCompoundDrawableTintMode`方法是在API23才能才加入其中的，直接使用在低版本的机器上便会导致崩溃，应当做好版本的判断进行兼容处理。
   ![20161230153448.png](../../../../../Pictures\20161230\20161230153448.png)  
   而`setCompoundDrawables`的从API1便加入了。而`setCompoundDrawables`方法要求必须先为drawable通过setbound方法设置大小。  
   ![20161226162506.png](../../../../../Pictures\20161226\20161226162506.png)

2. 让TextView的内容可以选择复制。
  1. 在xml文件中设置`android:textIsSelectable`的值为true即`android:textIsSelectable="true"`
  2. 代码中调用`tv.setTextIsSelectable(true);`设置TextView的内容可复制。  


> update 2016/12/23

 1. 设置字体大小和颜色
```
SpannableString tss = new SpannableString("已开"+ getGroup(groupPosition).getCourseList().size() + "班");
tss.setSpan(new AbsoluteSizeSpan((int) activity.getResources().getDimension(R.dimen.sc_group_textsize)), 2, tss.length() - 1,Spanned.SPAN_INCLUSIVE_EXCLUSIVE);
tss.setSpan(new ForegroundColorSpan(activity.getResources().getColor(R.color.real_red)), 2, tss.length(),Spanned.SPAN_INCLUSIVE_INCLUSIVE);
holder.tvClassCount.setText(tss);
```

3. TextView的内容可滑动
  1. xml中TextView添加属性`android:scrollbars="vertical" android:fadeScrollbars="false"`
  2. activity中为该TextView设定`tvTeacherClassClassDetailRemark.setMovementMethod(ScrollingMovementMethod.getInstance());`


4. TextView设置字体颜色大小
TextView可以直接设置HTML的内容
```
String source = "<font color='gray'>你好，我是HTML文本标签</font>"
Spanned span;
if(Build.VERSION.SDK_INT>=24){
          spanned=Html.fromHtml(source,Html.FROM_HTML_MODE_COMPACT);
  }else{
          spanned=Html.fromHtml(source);
  }
tv.setText(span);
```

> 注意使用该方法是无法通过font的size属性设置文字大小的，如果需要设置大小只能通过small标签，如`"<font color='gray'><small>我是小字体</small></font>"`