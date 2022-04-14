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