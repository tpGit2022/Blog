1. 查看Cygwin版本
`cygcheck -c cygwin`
2. 查看gcc版本
`gcc --version`
查看 g++，make，gdb同理。

```
autoconf2.1、automake1.10、binutils、gcc-core、gcc-g++、gcc4-core、gcc4-g++、gdb、pcre、pcre-devel、gawk、make共12个包

binutils，gcc，make。
```

3. 设置环境变量

~~* 需求：需要把存放shell脚本的目录放置环境变量PATH，让脚本命令可以快速得到执行而不需要多次切换命令
*思路：Linux下一切皆文件，环境变量依赖`profile`的文件，需要所有用户生效修改`/etc/profile`文件，如果只需要当前用户生效修改用户目录下的`~/.bash_profile`文件，这里因为是Cygwin模拟环境采用后者。
* 根据` ~/.bash_profile`文件中注释的提示，追加自己的shell脚本目录。~~
```
LiunxEnv="/cygdrive/e/MyScript/Liunx/"
if [ -d "${LiunxEnv}" ] ; then
  PATH="${LiunxEnv}:${PATH}"
fi
```

~~为了让配置及时生效，终端中执行`source ~/.bash_profile`。之后再Cygwin终端里面可以运行xxx.sh命令，直接执行自己shell脚本目录下的xxx.sh脚本文件了。~~

> 注意LiunxEnv变量的定义前后不要有空格，同时注意路径的描述。之后引用的变量${LiunxEnv}为PATH追加新值

  ~~之后执行写好的脚本命令可以通过 `bash shell.sh` 或者 `sh shell.sh`。~~


update:2022-04-27
cywgin会读取系统的环境变量 所以只需要将Linux脚本添加到系统环境变量PATH中去就好了

4. 添加ssh，curl，wget功能
  为了方便登录远程的Linux主机需要ssh功能，于是打开cygwin的安装器，输入openssh，
点击一下变成选中install状态，之后下一步安装即可

 curl和wget的安装类似。

5. ssh登录远程主机
  查看用法得到如下结果
  ```
  usage: ssh [-46AaCfGgKkMNnqsTtVvXxYy] [-B bind_interface]
           [-b bind_address] [-c cipher_spec] [-D [bind_address:]port]
           [-E log_file] [-e escape_char] [-F configfile] [-I pkcs11]
           [-i identity_file] [-J [user@]host[:port]] [-L address]
           [-l login_name] [-m mac_spec] [-O ctl_cmd] [-o option] [-p port]
           [-Q query_option] [-R address] [-S ctl_path] [-W host:port]
           [-w local_tun[:remote_tun]] destination [command]
  ```

 使用实例 `ssh root@176.122.170.156 -p 27948`, -p 后面接端口号，@左侧的root代表用户@右侧代表主机的ip地址

 6. cygwin执行shell脚本时的$'\r'问题
  由于Linux和Windows的回车换行符号的表示并不一样，需要经过dos2unix处理回车换行
符，执行 dos2unix filename 即可。

> dos2unix 不是自带命令需要通过cygwin的安装器自己安装


7. 添加右键菜单

cywgin添加右键菜单自动切换目录较为繁琐。

先新建批处理脚本 `cygwin.bat` 输入以下内容

```
@echo off 

rem 设置标题
title ClientWithThisTitleWillBeKill

rem 切换路径至 app 执行文件所在地

cd /d "D:\cygwin64\bin"

rem 启动 app 提示
echo 正在启动 Cygwin， 请稍候....

rem 启动逻辑 注意启动后调用 killexe 完成终端窗口的关闭

set script_exec_path=%*

mintty.exe -i /Cygwin-Terminal.ico - | %MyWinScriptHome%\KillEXE.exe
```

上述批处理用 `script_exec_path` 来接收右键菜单传递过来的路径

修改注册表添加菜单,保存如下代码为 `git_right_menu.reg` 右键选择合并，将注册表条目添加系统

```
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\Directory\Background\shell\cygwin]
@="Open In Cygwin"
"Icon"="D:\\cygwin64\\Cygwin-Terminal.ico"

[HKEY_CLASSES_ROOT\Directory\Background\shell\cygwin\command]
@="E:\\MyIT\\MyShell\\WindowsBAT\\00.AppLaunchs\\cygwin.bat %v" 

```

`Icon` 指向 Cygwin的图标，command指向上一步编写的 `cygwin.bat`脚本路径

在cygwin的 `$HOME` 中的 `.bash_profile` 文件中最后面添加如下代码:

```
# recive param when script exec from right_menu
if [ ! -n "${script_exec_path}" ]; then
script_exec_path="/cygdrive/c/Users/Walkers/Desktop/"
fi

if [ "${script_exec_path}" = "" ]; then
script_exec_path="/cygdrive/c/Users/Walkers/Desktop/"
fi
cd "${script_exec_path}"
# add extra environment
#LiunxEnv="/cygdrive/e/MyIT/MyShell/LinuxShell/002.Git/:/cygdrive/e/MyIT/MyShell/LinuxShell/"
#if [ -d "${LiunxEnv}" ] ; then
#  PATH="${LiunxEnv}:${PATH}"
#fi
```

上述代码在Win+R的执行的cygwin.bat会自动切到桌面下