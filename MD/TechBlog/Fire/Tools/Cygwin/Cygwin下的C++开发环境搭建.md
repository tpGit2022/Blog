需要的依赖库

需要的编译工具：devel下gcc-core,gcc-g++,make,gdb,binutils 

autoconf，automake，libtool，boost，libcurl
autoconf2.1 automake1.10 gcc4-core gcc4-g++ pcre pcre-devel gawk

# 错误
```
win32/jni_md.h:34:9: error: unknown type name '__int64'
```

解决方法：`-D__int64="long long"`

`Intellij idea 出现错误 error:java: 无效的源发行版: 8解决方法`
项目的jdk不对，File-setting-Build-Compiler-java compiler
project bytecode version 选择合适的jdk版本

# 参考资料
1. [Windows下利用Cygwin搭建C/C++开发环境GCC](http://blog.sina.com.cn/s/blog_143cf62360102wrgd.html)
2. 