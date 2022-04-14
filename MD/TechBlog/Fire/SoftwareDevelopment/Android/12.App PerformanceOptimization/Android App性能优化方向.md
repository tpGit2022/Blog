> 性能指标：
> 1. 布局复杂度  
> 2. 耗电量  
> 3. 内存  
> 4. 网络  
> 5. 程序执行效率  
> 
> 

# 分析辅助工具
1. MAT(Memory Analyzer Tools)  
 `hprof-conv dump.hprof converted-dump.hprof  `

2. 命令行模拟低内存环境被回收资源  
 将应用打开后按Home键让应用出于后台，执行`adb shell am kill youapppackagename`  
在windows环境可以使用如下命令 `for /L %i in (0,1,20) do adb shell am kill yourapppackagename` 多次执行`am kill` 命令
 
# 参考资料  
## 博客文献
1. [谷歌官方性能优化建议](https://developer.android.google.cn/training/best-performance.html)
2. [Android最佳性能优化实践(一)--合理管理内存-郭霖](http://blog.csdn.net/guolin_blog/article/details/42238627/)  
2. [Android最佳性能实践（二）--分析内存使用情况](http://blog.csdn.net/guolin_blog/article/details/42238633)  
3. [Android最佳性能实践（三）--高性能编码优化](http://blog.csdn.net/guolin_blog/article/details/42318689)  
4. [Android最佳性能实践（四）--布局优化技巧](http://blog.csdn.net/guolin_blog/article/details/43376527)  
2. [Android的性能优化](http://blog.csdn.net/MeloDev/article/details/51038694)  
3. [Android性能优化总结](http://blog.csdn.net/woyaowenzi/article/details/9273839)  
4. [Java性能调优](http://blog.csdn.net/lilu_leo/article/details/8115612)  

## 书
1. Efficient Java  
2. 