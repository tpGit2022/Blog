[TOC]


> 记录使用Linux中碰到的问题

1. shell中获取时间日期

```
$ date +%Y.%m.%d-%H:%M:%S
2019.01.07-08:27:37
time=$(date "+%Y-%m-%d %H:%M:%S")
echo $time
```

Y:年份 m:月份  d:日期 H:小时 M:分钟 S:秒

https://blog.csdn.net/sjin_1314/article/details/8561734


2. SCP
远程主机和本地主机之间拷贝文件

scp -P port local_file_path remote_username@remote_host_ip:remote_file_path

实例

`scp -P 2358  . root@123.1.2.3:/mnt/sdcard/`

#压缩
tar -czvf ***.tar.gz
tar -cjvf ***.tar.bz2
#解压缩
tar -xzvf ***.tar.gz
tar -xjvf ***.tar.bz2

递归修改目录和子目录

chmod -R xxx filename


7 = 4 + 2 + 1

r:4 w:2 x:1

ps aux

> ps -aux 会提示警告，- 是不必要的 


3. 让任务一直在后台运行
ssh开启的终端，退出终端的时候关联的任务会中断。如果需要断开和vps链接而保持后台运行，需要借助第三方工具，比如screen。

```
# install screen
yum install screen

# start a screen session
screen -S scree_session_name

# query all screen session
screen -ls

# to save cureent screen session, use keyboard like ctra+a then press d to save

# restore a screen session
screen -r screen_session_name

# restore a screen session with serialNum
screen -x screen_session_num

# exit a screen session
screen -d screen_session_name

# complete exit a screen seesion, enter screen session and input exit command
exit
```


# 加解压
gzip
`gunzip -k filename.gz` -k 保留源文件，默认会删除源文件


# 参考资料
1. [linux下tar.gz、tar、bz2、zip等解压缩、压缩命令小结](https://www.jb51.net/LINUXjishu/43356.html)

# 挂载磁盘

```
#! /bin/sh
echo begin to mount local disk


function mount_local_disk ( ) {
    echo $1,$2
    ## if dir is not exist, create it
    if [ ! -d $2 ]; then
        echo dir is not exist, create it
        mkdir $2
    fi
        echo dir is exist
    ## if $1 is not mount, mount it
    sudo mount $1 $2

}


mount_local_disk /dev/sdb3     /mnt/Software
mount_local_disk /dev/sdb10    /mnt/DiskSdk
mount_local_disk /dev/sdb2     "/mnt/E(Code)"
mount_local_disk /dev/sdb5     "/mnt/Heaven&Hell"
mount_local_disk /dev/sdb4     /mnt/Virtual
mount_local_disk /dev/sdb1     /mnt/D
mount_local_disk /dev/sda3     /mnt/C
```

# 字符串拼接

被拼接的字符串需要用 `${var}` 的形式

```
var="aaaa"
var2="ssss"${var}"hhh"
```

# 终端多行输入

`'` 或者 `"` 亦或者 `/` + enter 也就是 输入 \然后按回车键


多行注释

```
<<'COMMENT'
...
your Linux Shell Code
...
COMMENT
```

# 获取工作目录和脚本存储目录

* 获取工作路径 `$(pwd)`
* 获取脚本存储目录

```
$(cd `dirname $0`;pwd)
```

# 将命令结果赋值给变量 

反引号

```
query_result=`adb shell pm path ${pg}`
```

# su命令

su 命令一般是用于切换用户身份，在Linux中使用更频繁的应该是sudo，而在Android中直接执行 su 切换至 root身份，但在写脚本中这样的方式并不方便更期待的效果以root身份指定特定命令后自动退出root，

`adb shell su -c ls -al /data/data/xxxx`

-c 后面的命令并不需要反单引号，不要写成以下方式
```
adb shell su -c `ls -al /data/data/xxxx`
```