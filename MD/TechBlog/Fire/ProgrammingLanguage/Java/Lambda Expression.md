Lambda Expression 拉姆达表达式。

Android Studio添加Lambda Expression规则如下：
module级别的build.gradle首先添加java 8.0支持。
```
android {
    ...
    defaultConfig {
        ...
        //为了使用java 8.0
        jackOptions {
            enabled true
        }
        ....
    }
    ...
    ...
     compileOptions {
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }
    ....
}
```

> 注意Android Studio2.3 版本开启了java 8.0 会导致Data Binding library找不到BR类引起错误。

# 参考资料
1. [Google官方：使用 Java 8 语言功能](https://developer.android.com/guide/platform/j8-jack.html?hl=zh-cn)