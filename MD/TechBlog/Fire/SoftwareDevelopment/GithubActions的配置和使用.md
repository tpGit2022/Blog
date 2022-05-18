[TOC]

# 概述

Github Actions 原本是Github推出的用于持续化集成的一套工具，基于此发挥想象可以执行自己的应用，相当于白嫖Github的服务器，功能上有点类似于腾讯的云函数

Github Action 支持的更为广泛

YAML 文件是构建配置文件，git仓库下的会存在一个 `.github` 文件夹，当在GitHub上执行Action时会执行 `.github`文件夹下的所有 `.yml` 文件


先 Java 运行环境执行jar包


添加 Secret，

![abs_2022_05_11_09_15_38_0392.bmp](E:/MyIT/Blog/MD/TechBlog/Pictures/202205/abs_2022_05_11_09_15_38_0392.bmp)


发送邮件的完整实例

```
name: Action-Send Email

on: [push]

jobs:
  bot:
    runs-on: ubuntu-latest
    steps:
      - name: 'Checkout codes'
        uses: actions/checkout@v1
      - name: 'Send mail'
        uses: dawidd6/action-send-mail@v3.6.1
        with:
          server_address: smtp.139.com
          server_port: 465
          username: ${{ secrets.EMAIL_139_USER_NAME }}
          password: ${{ secrets.EMAIL_139_USER_PWD }}
          subject: Github Actions job result
          html_body: file://file_list.html
          body: github action send email test!!!!
          to: xxxxxxxx@qq.com
          from: GitHub Actions
```

`html_body` 的 value部分 file的起始点仓库根目录。

> 注意 python xxx.py 和 python xxxx\xx.py 时生成文件的不同位置

可以执行以下 Action来获取执行后的目录结果

```
	- name: '生成当前文件列表'
      run: bash ./listdir.sh

```

`listdir.sh` 的内容如下:

```shell
#!/bin/sh

ls -alR
```



python 环境设置

https://github.com/marketplace/actions/setup-python


邮件发送

https://github.com/marketplace/actions/send-email



```
Error: Message failed: 550 2f33627b5ecbec6-ffa92 Mail rejected
```

上述错误说明发送邮件失败，SMTP 500 可能是SMTP服务的原因，实测中发现139信箱容易出现该错误，


***TODO***

1. 挂载有道云笔记的每日签到
2. 挂载v2ray账号的每日签到
3. jd的签到


# 邮件知识扩展


常见的邮箱协议有 SMTP、POP3、IMAP等。乍一看，很难看出各自有什么作用。其实看一下全称就很容易了。

1.Simple Mail Transfer Protocol（SMTP）

2.Post Office Protocol 3（POP3）

3.Internet Mail Access Protocol（IMAP）

简单地说，SMTP管着发邮件，POP3/IMAP4管收邮件

[常用邮箱的服务器(SMTP/POP3)地址和端口整理](https://blog.51cto.com/u_15300443/3091999)

## 139

| 服务器 | 地址 | 端口(不带SSL) | 端口(带SSL) |
| :---:|:---:|:---:|:---:|
| POP3服务器 | pop.139.com | 110 | 995 |
| SMTP服务器 | smtp.139.com | 25 | 465 |
| IMAP服务器 | imap.139.com | 143 | 993 |




# 示例

```yaml
name: Python CI

on: 
    push:
    schedule:
    - cron: '30 1 * * *'
    - cron: '50 12 * * *'
    - cron: '25 7 * * *'

jobs:
  bot:
    runs-on: ubuntu-latest
    steps:
      - name: 'Checkout codes'
        uses: actions/checkout@v3
      
      - name: '安装Python环境'
        uses: 'actions/setup-python@v3'
        with: 
            python-version: 3.9
        
      - name: "配置依赖"
        run: pip install -r requirements.txt
        #run: pip install requests
      - name: "数据抓取测试"
        run: python3 ./01.Python/test.py
      - name: '生成当前文件列表'
        run: bash ./listdir.sh
      - name: 'Send filelist mail using 163'
        uses: dawidd6/action-send-mail@v3.6.1
        with:
          server_address: smtp.163.com
          server_port: 465
          username: ${{ secrets.EMAIL_163_USER_NAME }}
          password: ${{ secrets.EMAIL_163_USER_PWD }}
          subject: the file list about the compile
          body: Github Action Send File List
          html_body: file://file_list.html
          #html_body: file://2022_05_11.html
          #to: tp232fs234@chacuo.net
          to: ${{ secrets.EMAIL_ADDRESS_FOR_NOTIFY }}
          from: ${{ secrets.EMAIL_SEND_NAME }}

```


# 参考资料

1. [Docs-Github Actions-使用 Gradle 构建和测试 Java](https://docs.github.com/cn/actions/automating-builds-and-tests/building-and-testing-java-with-gradle)
2. [MayoBlueSkyMy-Actions](https://github.com/MayoBlueSky/My-Actions/tree/master)
3. [Github-Action-加密机密](https://docs.github.com/cn/actions/security-guides/encrypted-secrets)
4. [GitHub Actions 入门教程](https://www.ruanyifeng.com/blog/2019/09/getting-started-with-github-actions.html)
5. [Github-Action-定时任务](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#scheduled-events-schedule)
6. [Github-Action-定时任务-CN](https://docs.github.com/cn/actions/using-workflows/events-that-trigger-workflows)

