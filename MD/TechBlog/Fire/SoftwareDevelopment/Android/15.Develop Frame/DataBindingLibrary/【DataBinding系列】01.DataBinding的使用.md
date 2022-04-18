#　搭建DataBinding的环境

模块级别的build.gradle中，打开数据绑定开关：

```
android{
    ....
    dataBinding {
        enabled=true
    }
    ...
}
```

>  ***注意：***
>  1. 为了启用DataBinding，gradle plugin至少要是1.5.0.alpha1以上. Data Binding Library可以自Android2.1(API level 7+)上面使用。
>  2. 如果该模块依赖的library使用DataBinding，该模块也需要启用DataBinding功能。


新增的 library

![20200112154418.png](../../../../../Pictures/202001/20200112154418.png)



# 编写第一个布局文件

使用DataBinding，布局文件的写法和以往的布局文件不大一样。例子如下：
先创建实体类(com.leemoaly.databindingdemo.bean.User)

```
public class User {
    public final String firstName;
    public final String lastName;

    public User(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    public String getFirstName() {
        return firstName;
    }

    public String getLastName() {
        return lastName;
    }

}

```

编写布局文件(activity_third.xml)：

```
<?xml version="1.0" encoding="utf-8"?>
<layout xmlns:android="http://schemas.android.com/apk/res/android">
    <data>
        <variable
            name="user"
            type="com.leemoaly.databindingdemo.bean.User"></variable>
    </data>
    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:orientation="vertical">
        <TextView
            android:layout_width="match_parent"
            android:layout_height="60dp"
            android:text="{@user.firstName}" />
        <TextView
            android:layout_width="match_parent"
            android:layout_height="60dp"
            android:text="{@user.lastName}" />
    </LinearLayout>
</layout>
```

新建布局文件成功后，rebuild以下项目，在`app\build\generated\source\apt\debug\com\leemoaly\databindingdemo\databinding`目录下可以看见生成的类`ActivityThridBinding`。

> 生成类名的规则：以布局文件名为基础，转化为帕斯卡命名法(Pascal case:所有单词首字母大写)并加上Binding后缀。布局文件名中的下划线_会被当成单个单词的分割线去掉，如布局文件activity_third_hello会生成ActivityThirdHelloBinding.java文件。
> ***注意*** 用于Text中的javaBean的属性值必须为String即text可接受的类型，javabean如果是int，long之类的会导致报错。
> 如果javabean自己有生成get方法，在布局文件@{user.xxx}时会有两个提示。

可以为生成的类指定类名通过data节点的class属性：

```
<data class=".activityfour">
      ....
</data>
```

将生成activityfour类而不是ActivityThridBinding。不过这个不是很建议使用，特别是前期没指定class后期更改，为了保证代码的正常运行，你需要手动将代码里面的所有的ActivityThridBinding改为activityfour。

随便新建一个activity，名称随意，在activity的onCreate方法添加如下代码：

```
 @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        ActivityThridBinding binding= DataBindingUtil.setContentView(this,R.layout.activity_thrid);
        User user=new User("Lee","moaly");
        binding.setUser(user);
    }
```

POJO (plain-old Java Object)

## 绑定事件


##　 如何调试

如果编译出错，log 日志的报错信息，即出错的代码行是指框架根据 xml 文件生成的 xxxBinding.java，，由于目前 Android Studio 尚不支持自动定位出错代码行，所以我们要手动去找该文件。xxxBinding.java 文件位置：将 AS 切换成 Project 视图 - 对应的 module（如 app）- build - intermediates - classes - debug - 对应的 package。

然后根据出错代码行，推测对应的 xml 文件中出错的位置。

1. include测试符号未成功
2. 事件处理的属性未成功


* 数学计算 + - / * %
* 字符串连接 +
* 逻辑 && ||
* 二进制 & | ^
* 一元 + - ! ~
* 位移 >> >>> <<
* 比较 == > < >= <=
* instanceof
* 组 ()
* 字面量 - 字符，字符串，数字， null
* 类型转换
* 函数调用
* 字段存取
* 数组存取 []
* 三元运算符 ?：

> 表达式在xml布局文件中使用部分符号需要转义，

| 符号 | 描述 | 转义字符 | 十进制 |
| :--:|:--:|:--:|:--:|
|   | 空格 | &nbsp; | &#160;
| <  | 小于号 | &lt; |   &#60;
\>  | 大于号 | &gt;   | &#62;
&  | 与号 | &amp;  | &#38;
"  | 引号 | &quot; | &#34;
‘  | 撇号 | &apos; | &#39;
×  | 乘号  | &times; | &#215;
÷  | 除号 | &divide;  |  &#247;

例子：
```
<data>
        <variable
            name="array"
            type="String[]"/>
        <variable
            name="list"
            type="List&lt;String&gt;"/>
</data>
```

>**注意**：List<String>中的尖括号均需要转义，同时转义之后虽然在布局中该处显示为红色但不会影响正常的编译。

# Expression Language 表达式
布局文件中的表达式和java表达式有很多相似之处；



# 注意
1. Data Binding Library 不支持merge节点。
2. 

# 参考资料
1. [Data Biding Library官方指导文档](https://developer.android.google.cn/topic/libraries/data-binding/index.html)
1. [搞定Android DataBinding-00](https://yanlu.me/android-databinding-tutorial-00/)
2. [Android Data Binding 系列(一) -- 详细介绍与使用](http://connorlin.github.io/2016/07/02/Android-Data-Binding-%E7%B3%BB%E5%88%97-%E4%B8%80-%E8%AF%A6%E7%BB%86%E4%BB%8B%E7%BB%8D%E4%B8%8E%E4%BD%BF%E7%94%A8/)
3. [(译)Data Binding 指南](http://yanghui.name/blog/2016/02/17/data-binding-guide/?utm_source=tuicool&utm_medium=referral)
4. [精通 Android Data Binding](https://github.com/LyndonChin/MasteringAndroidDataBinding/blob/master/README.md)
5. [Android Data Binding（数据绑定）用户指南](http://www.jianshu.com/p/b1df61a4df77)
6. [Data Binding Library官方API文档](https://developer.android.google.cn/reference/android/databinding/package-summary.html)
7. [[Android]Data Binding（数据绑定）用户指南](http://blog.qiji.tech/archives/7506)
8. [Android Data Binder 的一个bug](http://blog.csdn.net/feelang/article/details/46342699)
9. [DataBinding的Google官方教程](https://developer.android.google.cn/topic/libraries/data-binding/index.html)  
10. [完全掌握Android Data Binding](http://www.jcodecraeer.com/a/anzhuokaifa/androidkaifa/2015/0603/2992.html)  
11. [Android DataBinder的一个Bug](http://blog.csdn.net/feelang/article/details/46342699)