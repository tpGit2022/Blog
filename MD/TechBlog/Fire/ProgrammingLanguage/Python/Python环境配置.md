[TOC]

* pip下载慢问题
	- 可添加国内源，在 `C:\Users\xxx` 目录下新建 pip 文件夹，在pip目录下新建pip.ini文件，文件内容如下:
	- ```
	- [global]
		index-url = https://pypi.tuna.tsinghua.edu.cn/simple
		[install]
		trusted-host=mirrors.aliyun.com
	- ```

	针对临时需要可以加上 `-i` 参数，例如
	`pip install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple`

* Python2和Python3共存问题

1.安装过程中可以手动选择安装路径，本文中的安装路径为"D:\python2", "D:\python3"。

2. 设置环境变量
为了使系统能够识别到python，可以便于在DOS窗口中直接命令行进入python环境，将python的安装路径写入系统变量。
1）写python3的环境变量
高级系统设置，环境变量，选择Path，点击编辑，新建，分别添加D:\python3和D:\python3\Scripts到环境变量。
2）写python2的环境变量
高级系统设置，环境变量，选择Path，点击编辑，新建，分别添加D:\python2和D:\python2\Scripts到环境变量。

3. 修改python编译器名
为了在DOS中便于区分python2和python3，我们将默认的python编译器名称进行修改。在python2和python3的安装目录中：
修改D:\python2中python.exe和pythonw.exe的名称为python2.exe、pythonw2.exe；
修改D:\python3中python.exe和pythonw.exe的名称为python3.exe、pythonw3.exe。

4. 设置pip
python 安装包需要用到包管理工具pip，但是当同时安装python2和python3的时候，pip只是其中一个版本，需重新分别安装两个版本的pip，使得两个python版本的pip能够共存。
安装pip2

```
python2 -m pip install --upgrade pip --force-reinstall
```

安装pip3

```
python3 -m pip install --upgrade pip --force-reinstall
```

可以使用pip2 -v和pip3 -v 分别查看pip信息，顺便检查是否成功安装。
之后就可以用pip2、pip3命令区分安装包所对应的python版本了。
比如，
pip2 install XXX
pip3 install XXX

# 参考资料

1. [python2和python3的共存](https://cloud.tencent.com/developer/article/1805279)
2. [pycharm下的多个python版本共存（一）](https://blog.51cto.com/lxw1844912514/2944876)
3. [pycharm下的多个python版本共存（二）](https://blog.51cto.com/lxw1844912514/2944880)
