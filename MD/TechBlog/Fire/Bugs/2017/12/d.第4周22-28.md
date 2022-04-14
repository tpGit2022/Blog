1.发生时间2.耗时3.描述4.解决思路5.解决方案 6.反思

# Bug概要
1. 发生时间:`2017-09-10 10:00:00`  耗时:`xxdxxhxxm`
2. 问题标签 `muldex`,`nullpoint`
3. 问题具体描述
4. 错误日志
***日志代码：***
```
Unable to find method 'com.android.build.gradle.api.BaseVariant.getOutputs()Ljava/util/List;'. Possible causes for this unexpected error include:
Gradle's dependency cache may be corrupt (this sometimes occurs after a network connection timeout.) Re-download dependencies and sync project (requires network)
The state of a Gradle build process (daemon) may be corrupt. Stopping all Gradle daemons may solve this problem. Stop Gradle build processes (requires restart)
Your project may be using a third-party plugin which is not compatible with the other plugins in the project or the version of Gradle requested by the project.
In the case of corrupt Gradle processes, you can also try closing the IDE and then killing all Java processes.
```
5. 原因分析

6. 解决方案
***解决方案代码:***
```

```
7. 参考资料
1. [](http://blog.csdn.net/yechaoa/article/details/78363911)
2. [](http://blog.csdn.net/ouyang_peng/article/details/52027668)



8. 反思和总结


```
Error:found unexpected optical bounds (red pixel) on top border at x=202.
Error:java.util.concurrent.ExecutionException: com.android.tools.aapt2.Aapt2Exception: AAPT2 error: check logs for details
Error:Execution failed for task ':realTime:mergeDebugAndroidTestResources'.
> Error: java.util.concurrent.ExecutionException: com.android.tools.aapt2.Aapt2Exception: AAPT2 error: check logs for details
```

解决方法：
在项目的gradle.properties中：
`android.enableAapt2=false`