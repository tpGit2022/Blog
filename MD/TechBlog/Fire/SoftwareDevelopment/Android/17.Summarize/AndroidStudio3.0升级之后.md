升级AndroidStudio3.0后项目出现了下面的一些问题

1. AAPT2 编译报错 AAPT2 error
```
Error:java.util.concurrent.ExecutionException: com.android.tools.aapt2.Aapt2Exception: AAPT2 error: check logs for details
```
解决在``中关闭appt2编译`android.enableAapt2=false`

2. apt插件问题
```
Error:Cannot choose between the following configurations of project :vitamio:
  - debugApiElements
  - debugRuntimeElements
  - releaseApiElements
  - releaseRuntimeElements
```
移除项目级别的`build.gradle`中的apt插件
```
dependencies {
        classpath 'com.android.tools.build:gradle:3.0.1'
        //移除下面的插件
//        classpath 'com.neenbedankt.gradle.plugins:android-apt:1.8'
        // NOTE: Do not place your application dependencies here; they belong
        // in the individual module build.gradle files
    }
```

另外如果使用了黄油刀ButterKnife的apt插件的需要调低版本之8.4.0,否则会导致编译失败