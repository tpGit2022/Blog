

  使用最新的SDK 中tool中的Monitor一直无法正常打开，提示错误，错误日志位于xxxx
之后去改目录查看只发现一堆的not found，can't resolve 等提示，google该问题
1. 有人说是java9，monitor无法正常加载java9，于是在启动批处理里面加入了修改Java_Home指向了Java8依旧无法正常加载
2. 另外一个说是jre，只要把Android的jre拷贝到monitor.exe所在的目录就行了，尝试之可行启动成功
  
