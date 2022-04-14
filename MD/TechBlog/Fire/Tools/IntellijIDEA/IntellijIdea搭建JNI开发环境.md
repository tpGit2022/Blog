搭建JNI环境常用的包 ***autoconf2.1、automake1.10、binutils、gcc-core、gcc-g++、gcc4-core、gcc4-g++、gdb、pcre、pcre-devel、gawk、make***


```
javac 命令：将.java源文件编译成.class字节码文件 
javac src/com/wenld/jnidemo/HelloWorld.java -d ./bin 
-d 表示将编译后的 class 文件放到指定的目录下

javah -jni 命令：根据class字节码文件生成.h头文件 
javah -jni -classpath ./bin -d ./jni com.wenld.jnidemo.HelloWorld 
默认生成的.h头文件名为：com_study_jnilearn_HelloWorld.h（包名+类名.h），也可以通过-o参数指定生成头文件名称： 
javah -jni -classpath ./bin -o HelloWorld.h com.wenld.jnidemo.HelloWorld

classpath：类搜索路径，这里表示从当前的 bin 目录下查找
d：将生成的头文件放到当前的 jni 目录下
o：指定生成的头文件名称，默认以类全路径名生成（包名+类名.h）
```


# 参考资料
1. [Win7 Android开发环境搭建之二(NDK+CDT)](http://evoupsight.com/blog/2014/03/18/android-install-ndk-cdt/)
2. [Cygwin编译JNI的环境配置](https://blog.csdn.net/zhangrui1209/article/details/42966119)
3. [IntelliJ IDEA平台下JNI编程（一）—HelloWorld篇](https://blog.csdn.net/huachao1001/article/details/53906237)
4. [Android NDK开发之旅(2)：Android Studio中使用CMake进行NDK/JNI开发(初级)](https://blog.csdn.net/AndrExpert/article/details/72904462)