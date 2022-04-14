Help-Edit Custom VM Options

各部分参数说明:

-Xmx Java Heap即堆内存的最大值，默认值是物理内存的1/4
-Xms Java Heap即堆的初始化内存大小


.Xms1024m,最小内存设置1G
  2.Xmx4096m,最大内存设置4G,原因本人工作用电脑内存8G
  3.MaxMetaspaceSize=512m,元数据区,jdk8前是方法区内存大小
  4.UseConcMarkSweepGC,设置年老代为并发收集
  5.SoftRefLRUPolicyMSPerMB=50,"软引用"的对象在最后一次被访问后能存活50毫秒
  6.PrintGC,每次GC时打印相关信息 
  7.PrintGCDetails,每次GC时打印详细信息

  # 参考资料
  1. [IntelliJ IDEA 设置 JVM 运行参数](http://blog.csdn.net/kl28978113/article/details/53031710)
  2. 