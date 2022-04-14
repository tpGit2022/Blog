> Ubuntu下使用shadowsocks直接使用的配置文件，而经常性的shadowsock所提供的是包含shadowsocks服务器信息的二维码图片，该工具实现二维码的扫描生成配置文件的功能。
# 功能点及实现思路

1. 功能点：扫描当前窗体获取二维码信息
    思路:直接将当前窗体截图保存，识别该截图便可获取图中包含的二维码信息
2. 功能点：二维码解码
    思路：二维码的本质是字符串，而shadowsocks的二维码信息常以ss://开头，采用Base64编码服务器地址端口以及密码信息。使用Google的zxing进行二维码解析，另外项目使用eclipse开发处理zxing的核心jar包还需要javase的jar包。
3. 功能点：选取本地二维码图片或者是网络链接识别二维码
    思路：

# 参考资料
1. [Base64编码原理解析与Java实现](http://www.imooc.com/article/9761)  
2. [Java做Base64编码和解码](http://outofmemory.cn/code-snippet/1604/java-do-base64-coding-jiema-wuxu-refer-renhe-leiku)  
3. [Java截取全屏代码](http://blog.csdn.net/yubo_725/article/details/46503669)
4. [【字符编码】字符编码&&Base64编码算法](http://www.cnblogs.com/leesf456/p/5288383.html)