添加依赖：
```
compile "com.square.okhttp:okhttp:2.1.2"
```

主要几点：基本请求，缓存配置，拦截器，https

即官网的`Calls,Connections,Recipes,Interceptors,HTTPS`

核心类：`OkHttpClient,Request,Call,Response,Interceptor`


  OKHttp POST请求的响应体的结果是乱码，在排除了返回结果的编码问题后google相关问
题得到可能性之一请求设置了 "addHeader(“Accept-Encoding”, “gzip”)",移除之后发现正常了，继续深入了解得知

加入如上的请求头 `addHeader(“Accept-Encoding”, “gzip”)`, 

```
When you provide your own Accept-Encoding header you’re instructing OkHttp that you want to do your own decompression. By omitting it, OkHttp will take care of both adding the header and the decompression.

```


HttpUrl

```
HttpUrl.Builder httpBuild = HttpUrl.parse(url).newBuilder();
httpBuild.addQueryParameter("username", "admin");
httpBuild.addQueryParameter("password", "admin");
requestBuild.url(httpBuild.build());
```


# 参考资料
1. [OkHttp基本使用](http://www.jianshu.com/p/14243df250da)
2. [android okhttp 3.8.0版本的使用](http://itsayer.com/?p=318)
3. [《第一行代码》笔记(8)——OkHttp的简单使用](http://www.th7.cn/Program/Android/201707/1211293.shtml)
4. [读OkHttp3文档记录](http://blog.csdn.net/tan958013863/article/details/73920331)
5. [Okhttp使用详解](http://blog.csdn.net/iispring/article/details/51661195)
6. [OkHttp官方教程解析-彻底入门OkHttp使用](http://blog.csdn.net/mynameishuangshuai/article/details/51303446)
7. [OKHTTP之缓存配置详解](OKHTTP之缓存配置详解)
8. [OkHttp 官方中文文档](http://blog.csdn.net/jackingzheng/article/details/51778793)
9. [从原理角度解析Android （Java） http 文件上传](http://blog.csdn.net/lmj623565791/article/details/23781773)
10. []()