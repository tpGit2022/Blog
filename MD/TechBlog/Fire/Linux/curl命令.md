curl 命令用于从服务器获取数据或者上传数据至服务器。

curl --help 查询curl的用法， curl的命令格式如下：

`curl [options] <url>`

url是必选项，option选择很多下面说一说常见的选项：

> 选项区分大小写

-o <file> : 指定输出的文件名称

`curl -o baidu.html https://www.baidu.com`

-A <name> : 指定user-agent 

`curl -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"`

-H <head/@file> : 配置请求头

```
curl -H "Accept-Language: zh-CN,zh;q=0.9" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8" -H "Accept-Encoding: gzip, deflate, br" -H "X-Client-Data: CKS1yQEIjLbJAQijtskBCMG2yQEIqZ3KAQioo8oBCOKoygEY+aXKAQ=="
```

-e <url> : 指定Referer 

```
curl -e "https://www.baidu.com"
```

-x [protocol://]host[:port] : 设置代理

```
curl -x 127.0.0.1:1080
```

-# 