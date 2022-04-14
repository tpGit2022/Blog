

基本使用的内容
1. 基本的get，post等操作
2. 代理设置，请求头部的设置，超时设置，编码问题
3. post请求的表单，提交
4. cookie的处理
5. 

get/post中的常用配置
proxies  代理设置
headers  请求头部信息
data     post中的data数据体
cookies  cookie信息
file     post请求中添加file文件
verify   关闭https验证

代理设置样例
```
proxies = {
    "http": "http://xxx.xxx.xx.xxx:xxxx",
    "https": "http://xxx.xxx.xx.xxx:xxxx"
}
request_content = requests.get(url, proxies=proxies)
```

# 参考资料
1. [Requests的官方文档](http://www.python-requests.org/en/master/)
2. [Requests开速上手](http://docs.python-requests.org/zh_CN/latest/user/quickstart.html)
3. [关于requests的session方法保持cookie的问题](http://blog.csdn.net/falseen/article/details/46962011)