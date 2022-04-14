[TOC]
   
# 超过64K方法数限制
1. 发生时间:`2017-08-08 10:00:00`  耗时:`30min`
2. 问题标签 `Android`  , `muldex`,`nullpoint`
3. 问题具体描述
4. 错误日志
***日志代码：***
```
Error:The number of method references in a .dex file cannot exceed 64K.
Learn how to resolve this issue at https://developer.android.com/tools/building/multidex.html
Error:Execution failed for task ':xxxprojectname:transformClassesWithDexForDebug'.
> com.android.build.api.transform.TransformException: com.android.ide.common.process.ProcessException: java.util.concurrent.ExecutionException: java.lang.UnsupportedOperationException
```
5. 原因分析
超出了Android系统的单dex文件64k限制。
6. 解决方案
按Google官方文档启动多dex配置。
***解决方案代码:***
```

```
7. 参考资料
    * `https://developer.android.com/tools/building/multidex.html`
8. 反思和总结