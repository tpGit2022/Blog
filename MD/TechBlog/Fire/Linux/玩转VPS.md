

  入手了一台海外的VPS主机安装上了CentOS(Community Enterprise Operating System)
系统，该系统是Linux的发行版之一,这篇博客主要是对这台VPS使用过程中的遇到问题的记录.

  为了管理方便第一项自然是远程管理Linux主机，为此需要借助SSH的功能，远程的VPS安
装CentOS系统安装openssh-server，本地主机Win10则利用Cygwin终端环境下的openssh远程管理VPS主机。

# 准备工作

  先确认远程的VPS是否已存在openssh-server，借助CentOS的内置yum命令查询当前系统
的软件包, `yum list installed | grep openssh`

> yum 只是Linux管理软件包的工具类似的还有Ubuntu下的apt，dpkg命令

  由于ssh远程Linux，出现的都是终端界面，为此编辑器Vi的基本操作非常有必要了解，
通过insert和esc键进入或者退出编辑模式。
  
# 远程工具OpenSSH

 ```
 ssh -p port username@ip
 ```

 port ssh登录端口
 username ssh登录用户名
 ip ssh登录的主机ip地址

  回车之后需要输入密码，输入的密码不会显示输入完成后回车确认。为了登录的方便我
们需要进一步简化登录的流程，借助"公私钥"认证方式可以实现ssh免密登录。实现ssh免密登录的核心步骤其实很简单，把客户端client的公钥放到vps服务器的authorized_keys文件就可以了，之后 `ssh -p port username@ip` 登录就不需要密码了，完整的流程如下

1. 客户端生成公私钥
   客户端通过 `ssh-keygen` 生成公私钥。 
   `ssh-keygen -t rsa` 一路回车生成公私钥

2. 服务器端加入客户端公钥
   这里利用cat将本地内容通过管道传送到远程服务器
   `cat ~/.ssh/id_rsa.pub | ssh -p xxx user@xxx.xxx.xxx.xxx 'cat >> /home/xxx/.ssh/authorized_keys'`
3. 服务器重启ssh服务
   `service sshd restart`

  ssh登录的日志会存储在服务器的 /var/log/secure/ ,如果ssh免密登录失败可以从这里
查看失败的原因从而去修整，这里列举下常见的原因导致的ssh免密登录失败：

1. 权限问题
  ```
  700 ~/.ssh
  600 ~/.ssh/authorized_keys
  ```

2. 服务器端相关配置没有打开
  /etc/ssh/sshd_config 中ssh登录的相关配置,去掉后面几项开头的#号

```
# Authentication:

#LoginGraceTime 2m
#PermitRootLogin no
#StrictModes yes
#MaxAuthTries 6
#MaxSessions 10

RSAAuthentication yes
PubkeyAuthentication yes
AuthorizedKeysFile      .ssh/authorized_keys
#AuthorizedKeysCommand none
#AuthorizedKeysCommandRunAs nobody
```

3. 本地生成公私钥时指定了文件名，登录失败需要密码
  如果你在公私钥生成阶段 `ssh-keygen -t rsa -f filepath`, 加了-f参数来表示存储的位置，那么在ssh登录远程主机的时候需要指定私钥的位置
`ssh -i filepath -p portnum username@ip`, filepath指向的私钥文件

4. 查看系统版本，系统位数之类的

```
uname -a
```

手机端管理远程VPS

  手机端也可以借助ssh来管理VPS，Android手机上被提得比较多的是ConnectBot和
JuiceSSH工具，考虑到JuiceSSH还区分免费和收费版就直接选择ConnectBot了。

  ConnectBot使用挺简单的先点击右上角的管理公钥，生成密钥然后考虑公钥，将公钥的
内容追加到远程VPS的 `/home/username/.ssh/authorized_keys` 文件中，之后就是主界面新建链接，然后配置中的使用公钥验证选择刚才新生成的密钥。

5. 新增用户

```
useradd newusername       //add a user name newusername
passwd newusername       // set password for newusername
userdel username        //del the username without home dir name  "username"
userdle -r username     //del the username with the home dir name "username"
```


# VPS的安全工作

 常见的VPS的安保工作有如下：
 1. 修改ssh的端口为其他不常见的端口
 2. 禁用root远程登录，禁用密码登录 开启ssh的rsa密钥验证登录
 3. 使用iptables

# 其他

1. 本地和远程主机文件传输
  主要是靠scp命令，将文件从前一个地址拷贝到后面的地址
`scp -P portNum local_file_path username@remote_host_ip:remote_file_path` 
`scp -P portNum username@remote_host_ip:remote_file_path local_file_path`

2. 离线运行程序
  ssh登录主机后，运行了程序，如果断开了ssh链接远程主机运行的程序也会停止，想要
程序在远程主机运行下去，可以借助 screen 软件，在screen开启的终端里面执行需要一直运行下去的程序，这样即便ssh断开了程序的运行也不会终止。

```
yum install screen //安装screen
screen -S name //开启一个name的终端回话，
screen -ls //查看所有screen的回话
screen -r name //重新连接上name的回话
screen -x num // 重新连上编号是num的回话
screen -d name // 关闭某个回话
```

具体的帮助文档 ：

```
Use: screen [-opts] [cmd [args]]
 or: screen -r [host.tty]

Options:
-4            Use IPv4.
-6            Use IPv6.
-a            Force all capabilities into each window's termcap.
-A -[r|R]     Adapt all windows to the new display width & height.
-c file       Read configuration file instead of '.screenrc'.
-d (-r)       Detach the elsewhere running screen (and reattach here).
-dmS name     Start as daemon: Screen session in detached mode.
-D (-r)       Detach and logout remote (and reattach here).
-D -RR        Do whatever is needed to get a screen session.
-e xy         Change command characters.
-f            Flow control on, -fn = off, -fa = auto.
-h lines      Set the size of the scrollback history buffer.
-i            Interrupt output sooner when flow control is on.
-l            Login mode on (update /var/run/utmp), -ln = off.
-list         or -ls. Do nothing, just list our SockDir.
-L            Turn on output logging.
-m            ignore $STY variable, do create a new screen session.
-O            Choose optimal output rather than exact vt100 emulation.
-p window     Preselect the named window if it exists.
-q            Quiet startup. Exits with non-zero return code if unsuccessful.
-r            Reattach to a detached screen process.
-R            Reattach if possible, otherwise start a new session.
-s shell      Shell to execute rather than $SHELL.
-S sockname   Name this session <pid>.sockname instead of <pid>.<tty>.<host>.
-t title      Set title. (window's name).
-T term       Use term as $TERM for windows, rather than "screen".
-U            Tell screen to use UTF-8 encoding.
-v            Print "Screen version 4.00.03 (FAU) 23-Oct-06".
-wipe         Do nothing, just clean up SockDir.
-x            Attach to a not detached screen. (Multi display mode).
-X            Execute <cmd> as a screen command in the specified session.
```


SS

```
killall ssserver
vi /etc/shadowsocks.json
ssserver -c /etc/shadowsocks.json -d start
ssserver -c /etc/shadowsocks.json -d stop
```