  HttpUrl是OKHTTP继承之Object用来URL描述统一资源定位符的。研究这个是出于Cookjar
的 loadForRequest(HttpUrl url) ，在多用户的cookie情况下希望通过HttpUrl来标记不同的用户以便载入正确的Cookies，对于多出来的UserID打算在拦截器中统一处理掉。

  要使用HttpUrl类得先对URL有所了解，URL是URI(统一资源标识符)的一部分，URI的格式
`URI = scheme://[userinfo@]host[:port]path[?query][#fragement]`

  一些URI的例子如下：
```
ftp://ftp.is.co.za/rfc/rfc1808.txt
http://www.ietf.org/rfc/rfc2396.txt
tel:+1-816-555-1212
telnet://192.0.2.16:80/
jdbc:datadirect:oracle://myserver:1521;sid=testdb
ssh://root@172.13.43.23:/mnt/
```
  
  这里HttpUrl代表是http和https的URL也就是scheme是http和https，一般http对应的por
t是80，http对应的port是443，URL里面的默认一般都会省略，userinfo在http和https的URL中是不必要的无需理会。
`http://square.github.io/okhttp/3.x/okhttp/okhttp3/HttpUrl.html#encodedFragment--`

上述的URL，scheme是http，`square.github.io` 是host，而 `okhttp/3.x/okhttp/okhttp3/HttpUrl.html` 是path，最后的`#encodedFragment--`就是fragment，fragment更类似目录里的超链接通过fragment可以快速完成页面内的跳转定位。

  了解了这些，HttpUrl的方法就很好懂了。下面列举几个常用的方法：

`HttpUrl parse(String url)`
解析url构建HttpUrl对象，内部调用下面的get方法来完成具体操作

`HttpUrl get(String url)`
解析url通过内部的Builder构造HttpUrl对象

`String username()`
返回用户名，如果存在的话

`String encodedUsername()`
返回编码后的用户名如果存在的话

`Builder newBuilder()`


`Builder newBuilder(String link)`

`String redact()`
返回scheme和host，其他成分被移除，path会被替换成/...
(不知道这个方法是干啥用的)

`HttpUrl resolve(String link)`


`String topPrivateDomain()`
返回host，如果host是ip返回null否则返回host

`boolean equals(Object other)`
HttpUrl的equal方法被复写过
```
@Override public boolean equals(@Nullable Object other) {
    return other instanceof HttpUrl && ((HttpUrl) other).url.equals(url);
}
```

`List<String> pathSegments()`
返回所有的path以List<String>的形势

`int pathSize()`
返回path填充的List<String>的长度

`String queryParameter(String name)`
查询key为name 的value

`queryParameterName(int index)`
返回query中index的key

`String queryParameterValue(int index)`
返回query中index的value

`List<String> queryParameterValues(String name)`
返回query中key为name的所有value，比如 `http://www.baidu.com?type=text&type=txt`queryParameterValues(type)，将会返回text和txt组成的List<String>

`URI uri()`
返回HttpUrl代表的uri

`URL url()`
返回HttpUrl代表的url


# 参考资料
1. [HttpUrl-Doc](http://square.github.io/okhttp/3.x/okhttp/okhttp3/HttpUrl.html)
2. [wiki-统一资源定位符](https://zh.wikipedia.org/wiki/统一资源定位符)
3. [wiki-URL](https://en.wikipedia.org/wiki/URL)
4. [RFC-URI](https://tools.ietf.org/html/rfc3986#section-1.1.1)