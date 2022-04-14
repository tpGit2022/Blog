
  配置多用户，在使用搬瓦工的vps，搭建后主机后左下方有安装shadowsock的按钮，不过
这里install的是单用户的，如果希望多弄几个shadowsock的账号就需要修改相关的配置了

  个人vps上面安装的Centos的Linux系统，后面一键安装的shadowsocks通过查询已安装的
软件包 `yum list installed` 得到如下结果

```
[root@host ~]# yum list installed | grep shad
shadow-utils.x86_64    2:4.1.5.1-5.el6  @anaconda-CentOS-201605220104.x86_64/6.8
```

  新增shadowsocks的用户配置文件 `/etc/shadowsocks.json`,

  ```
  {
 "server": "xxx.xxx.xxx.xx",
  "local_address": "127.0.0.1",
  "local_port": "1080",
  "port_password" : {
      "port1":"passwd1",
      "port2":"passwd2",
      "port3":"passwd3",
      "port4":"passwd4"
   },
   "timeout":300,
   "method":"aes-256-cfb",
   "fast_open":false
}
  ```

 shadowsocks服务器端用户相关配置说明：
 server：远程服务器地址，也就是vps主机的对外ip地址
 local_address：本地地址这里填写127也就是本地主机
 local_port：本地的端口号
 port_password：这里填写的端口和密码，是客户端需要填入用于验证的端口和密码
 timeout：超时时间
 method：加密方式

  添加完配置文件就需要应用配置文件了，这需要修改 `/etc/rc.local` 文件，一键安装shadowsock的配置里面有这样一句 
  ```
  [root@host ~]# cat /etc/rc.local
#!/bin/bash
touch /var/lock/subsys/local
/usr/bin/setterm -blank 0 || true

/usr/bin/ssserver -s ::0 -p `cat /root/.kiwivm-shadowsocks-port` -k `cat /root/.kiwivm-shadowsocks-password` -m `cat /root/.kiwivm-shadowsocks-encryption` --user nobody --workers 2 -d start
  ```
  
  这里看得出来是用过ssserver在手动设置用户密码等信息，通过查看ssserver -h的用法
  ```
  [root@host ~]# ssserver -h
usage: ssserver [OPTION]...
A fast tunnel proxy that helps you bypass firewalls.

You can supply configurations via either config file or command line arguments.

Proxy options:
  -c CONFIG              path to config file
  -s SERVER_ADDR         server address, default: 0.0.0.0
  -p SERVER_PORT         server port, default: 8388
  -k PASSWORD            password
  -m METHOD              encryption method, default: aes-256-cfb
  -t TIMEOUT             timeout in seconds, default: 300
  --fast-open            use TCP_FASTOPEN, requires Linux 3.7+
  --workers WORKERS      number of workers, available on Unix/Linux
  --forbidden-ip IPLIST  comma seperated IP list forbidden to connect
  --manager-address ADDR optional server manager UDP address, see wiki

General options:
  -h, --help             show this help message and exit
  -d start/stop/restart  daemon mode
  --pid-file PID_FILE    pid file for daemon mode
  --log-file LOG_FILE    log file for daemon mode
  --user USER            username to run as
  -v, -vv                verbose mode
  -q, -qq                quiet mode, only show warnings/errors
  --version              show version information

Online help: <https://github.com/shadowsocks/shadowsocks>
  ```

 从上面可以知道只需要使用-c选项就可以使用外部的配置文件来启用多用户了，于是修改/etc/rc.local 的文件内容。
 ```
 #!/bin/bash
touch /var/lock/subsys/local
/usr/bin/setterm -blank 0 || true

/usr/bin/ssserver -s ::0 -c /etc/shadowsocks.json --user nobody --workers 2 -d start
 ```

  之后执行reboot命令，重启服务器。

  

  
# 参考资料
1. [搬瓦工Shadowsocks安装及配置多用户(服务端)](https://blog.huihut.com/2016/12/03/BandwagonShadowsocksServer/) 