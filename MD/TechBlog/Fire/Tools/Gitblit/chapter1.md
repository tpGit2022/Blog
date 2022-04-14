常用于搭建私有Git服务器的软件。
*. **GitStack**
    目前已转收费，有Web页面和Gitlit类似。
*. **Gitblit**
    目前使用的方案，Web页面管理，清晰可见。
*. **COPSSH**
    最初找到的方案，弊端很多，没有web页面管理，不够直观，且操作繁琐的很，强烈反对使用该方式。
*. **Gitlab**

1. Gitblit是纯java的实现，需要java环境支持。首先你得拥有java环境，安装好jdk配置好环境变量才能进入下一步。
2. 下载Gitblit。http://gitblit.com  
![20170801164252.png](../../../Pictures\20170801\20170801164252.png)
下载Gitblit Go。下载完成后解压即可无需安装。解压后(1.8.0版本)  
![20170801164452.png](../../../Pictures\20170801\20170801164452.png)

先修改一下配置找到data文件夹下的gitblit.properties文件，在文件最后添加如下配置。
```
# 设定存放Git仓库的本地地址，绝对路径，注意使用/而不是\分割路径
git.repositoriesFolder=E:/Git/GitRespository
# 指定HTTP使用的端口
server.httpPort=10101
# 指定https使用的端口
server.httpsPort=10102
# 指定HTTP服务器地址，填入本机ip即可
server.httpBindInterface=192.168.2.70
# 指定HTTPS服务器地址，填入本机ip即可
server.httpsBindInterface=192.168.2.70
```

> 注：Gitblit的老版本可能找不到gitblit.properties只有defaults.properties，修改defaults.properties中相对应值即可。

修改完配置返回data上一目录双击运行gitblit.cmd,  
![20170801165536.png](../../../Pictures\20170801\20170801165536.png)  
运行脚本后，浏览器访问gitblit.properties配置的服务器地址。http://192.168.2.70:10101  
![20170801165611.png](../../../Pictures\20170801\20170801165611.png)  
如果你想访问https的，访问https://192.168.2.70:10102。
注意由于没有安装证书直接访问可能被浏览器拦截。

安装服务。
安装服务的目的在于 **你不需要每次进来运行gitblit.cmd脚本来开启git服务器,只要Gitblit服务开启再就可以直接访问搭建的git服务器**。
先右键编辑installService.cmd，看到的应该是这样的  
![20170801170325.png](../../../Pictures\20170801\20170801170325.png)  

需新增一个变量CD，修改两处的配置。
CD变量用于存储Gitblit所在的位置。
```
# 存放Gitblit的位置 注意分隔符号\
SET CD=D:\gitblit-1.8.0
# ARCH根据jdk的版本，jdk32位ARCH=x86,jdk64位，ARCH=amd64.
SET ARCH=amd64
# --StartParams置空
--StartParams=""
```

***特别说明***  

1.  ARCH 的取值决定于你的JVM位数也就是你安装的JDK位数。官方文档原话是
    `Set the ARCH value as appropriate for your installed Java Virtual Machine.`，所以认为ARCH取决于电脑系统的位数的说法是错的，ARCH取决于JDK的位数。
2. --StartParams 关于这个启动参数置空不要手贱在双引号中间加个空格，不然你的服务会一直启动不了。
就因为这个坑爹的空格，浪费了我两个小时。

> 安装服务是最容易出错的地方，你可以借助logs文件夹下的错误日志定位问题。

修改后的配置文件如下：  
```
@REM Install Gitblit as a Windows service.

@REM gitblitw.exe (prunmgr.exe) is a GUI application for monitoring 
@REM and configuring the Gitblit procrun service.
@REM
@REM By default this tool launches the service properties dialog
@REM but it also has some other very useful functionality.
@REM
@REM http://commons.apache.org/daemon/procrun.html

@REM arch = x86, amd64, or ia32
SET CD=D:\gitblit-1.8.0
SET ARCH=amd64


@REM Be careful not to introduce trailing whitespace after the ^ characters.
@REM Use ; or # to separate values in the --StartParams parameter.
"%CD%\%ARCH%\gitblit.exe"  //IS//gitblit ^
         --DisplayName="gitblit" ^
         --Description="a pure Java Git solution" ^
         --Startup=auto ^
         --LogPath="%CD%\logs" ^
         --LogLevel=INFO ^
         --LogPrefix=gitblit ^
         --StdOutput=auto ^
         --StdError=auto ^
         --StartPath="%CD%" ^
         --StartClass=org.moxie.MxLauncher ^
         --StartMethod=main ^
         --StartParams="" ^
         --StartMode=jvm ^
         --StopPath="%CD%" ^
         --StopClass=org.moxie.MxLauncher ^
         --StopMethod=main ^
         --StopParams="--stop;--baseFolder;%CD%\data" ^
         --StopMode=jvm ^
         --Classpath="%CD%\gitblit.jar" ^
         --Jvm=auto ^
         --JvmMx=1024

```
配置好后，右键管理员运行installService.cmd。直接运行于installService.cmd同目录的gitblitw.exe，  
![20170801203642.png](../../../Pictures\20170801\20170801203642.png)  

可以在windows的服务中看到Gitblit服务已开启  
![20170801203144.png](../../../Pictures\20170801\20170801203144.png)  
浏览器输入http://192.168.2.70:10101/，正常打开页面则服务运行正常。  
![20170801204121.png](../../../Pictures\20170801\20170801204121.png)  

这样在本机访问没有任何问题，在同一局域网其他机器访问出现问题，可能是因为防火墙导致的，将对应的端口添加至防火墙入站规则便可成功访问，步骤如下(以win为例)：
1. 控制面板-系统和安全-Windows防火墙-高级设置
2. 入站规则-新建规则-规则类型选择端口-规则应用于TCP，下方填入端口，端口号取决于你在gitblit.properties中设置的端口，默认为10101,10102,29418分别对应着http，https，ssh三种协议，之后一直点击下一步，下一步，最后填写名称和描述(内容自定)
![20170802173138.png](../../../Pictures\20170802\20170802173138.png)

>  搭好的git服务器可能出现自己其他人访问都正常，但别人无法ping通服务器，这同样是防火墙的缘故，依然进入高级防火墙设置在入站规则中找到"文件和打印机共享(回显请求-ICMPv4-In)",双击打开勾选已启用，点击应用，其他设备便可正常ping通服务器了。

# 参考资料
1. http://blog.csdn.net/smellmine/article/details/52139299
2. [gitblit官方文档](http://www.gitblit.com/setup_go.html)
3. [Apache Commons](http://commons.apache.org/proper/commons-daemon/procrun.html)
4. [gitblit无法安装windows服务或者启动服务失败：Failed creating java](http://aigo.iteye.com/blog/2260957)
5. 