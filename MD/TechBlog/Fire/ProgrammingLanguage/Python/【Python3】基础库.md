[TOC]


# 格式化输出

```
def print_info():
    index = 20
    while index < 1200:
        out_print_info = "name:{:d}\ttest:0x{:X}".format(index, index)
        print(out_print_info)
        print(f"name:{index}")
        index = index + 1
```

# 时间


# Json


# 正则


# 邮件发送

smtplib 邮件发送库。SMTP是邮件发送协议，POP3是邮件接收协议
email 邮件构建。


# 参考资料

1. [使用Python读取，写入和解析JSON](https://cloud.tencent.com/developer/article/1654900)