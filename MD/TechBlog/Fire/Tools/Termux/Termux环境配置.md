[TOC]

# 配置Java环境

`pkg install openjdk17`

安装完后执行 `java -version` 提示 `"libz.so.1" not found` GitHub搜索发现存在[该Issue](https://github.com/termux/termux-packages/issues/9866) 根据提示更新
`zlib`.

执行 `pkg upgrade zlib` 更新完后执行 `java -version` 正常运行

 ![abs_2022_04_26_19_39_04_0106.bmp](E:\MyIT\Blog\MD\TechBlog\Pictures\/202204/abs_2022_04_26_19_39_04_0106.bmp)


scp 复制文件

PC通过scp复制PC文件至手机

`tar zcf - /c/Users/Walkers/Desktop/TermuxConsole-0.0.3.jar | ssh 192.168.1.107 -p 8022 tar zxf - -C /data/data/com.termux/files/home`

![abs_2022_04_27_08_14_12_0109.bmp](E:/MyIT/Blog/MD/TechBlog/Pictures/202204/abs_2022_04_27_08_14_12_0109.bmp)  


PC 通过scp获取手机端文件

`ssh 192.168.1.107 -p 8022 "tar czf - ~/c/Users/Walkers/Desktop/TermuxConsole-0.0.3.jar" | tar xzvf - -C ./`  

![abs_2022_04_27_08_12_47_0910.bmp](E:/MyIT/Blog/MD/TechBlog/Pictures/202204/abs_2022_04_27_08_12_47_0910.bmp)  


# 参考资料

1. [ssh可以登录，但是scp不行，解决方案](https://blog.csdn.net/beyond__devil/article/details/55512414?utm_source=blogxgwz2)
2. [Termux 高级终端安装使用配置教程](https://www.sqlsec.com/2018/05/termux.html)
3. [Termux官网](https://termux.com/)
4. [Termux-Github地址](https://github.com/termux)