[TOC]


# 下载和OpenCV的配置

如果 OpenCV 需要协同开发，最好保证所用的 OpenCV 保持一致。 

配置环境变量

```
OPENCV_HOME   ------>    E:\MySDK\OpenCV\opencv

OPENCV_EXEC   ------->   %OPENCV_HOME%\build\x86\vc12\bin
```

以上根据项目需要配置是 x86 还是 x64

# VS相关配置

VS相关配置主要是以下三项

* 包含目录
	- 新增opencv的include的目录
	- 包含 E:\MySDK\OpenCV\opencv\build\include
	E:\MySDK\OpenCV\opencv\build\include\opencv
	E:\MySDK\OpenCV\opencv\build\include\opencv2
* 库目录
	- 包含 open 的lib目录
	- E:\MySDK\OpenCV\opencv\build\x86\vc12\lib
* 链接器-输入
	- 包含 opencv_wordldxxxd.lib
	- 譬如 E:\MySDK\OpenCV\opencv\build\x86\vc12\lib\opencv_world300d.lib


# 测试例子

```
code language:C++
#include <iostream>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>

using namespace cv;

int main()
{
	Mat img = imread("C:\\Users\\Walkers\\Desktop\\TP_IMAGE\\P2022-03-11-08_28_32.bmp");
	cvNamedWindow("图片");
	imshow("图片", img);
	waitKey(10000);
    std::cout << "Hello World!\n";
	return 0;
}
```


# Python 配置OPENCV

OpenCV 配置好后，Python 需要先通过 pip 下载以下三个包

```
pip install wheel
pip install numpy
pip install opencv-python
```

安装中可能速度很慢需要切换到国内的源，可使用以下命令

```
pip install wheel -i https://pypi.tuna.tsinghua.edu.cn/simple
```

安装完后在 python 的交互命令行中测试以下

```
Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import cv2
>>> cv2.__version__
'4.5.5'
>>>
```

若能正常显示 代表可以 opencv-python 已成功安装，针对 PyCharm 可能依旧导入爆红，需要在 File-Settings-Project-Python Interpreter中安装opencv-python包

Python 测试代码

```
import cv2


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    url = "rtsp://192.168.1.103:8554/teststream"
    cap = cv2.VideoCapture(url)
    print(cap.isOpened())
    while cap.isOpened():
        success, frame = cap.read()
        cv2.imshow("frame", frame)
        cv2.waitKey(1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
```


# C++ --> OpenCV::VideoCapture

# C++ --> OpenCV::Mat


OpenCV 也是有用到 FFMPEG 

# H265

OpenCV 3.0.0 直接解码不了

以下C++代码可能会长时间无响应

```
VideoCapture cap("rtsp://admin:123456@192.168.123.130:554/stream1");
	if (!cap.isOpened()) {
		std::cout << "开启失败" << std::endl;
		return;
	}
	Mat frame;
	if (!cap.read(frame)) {
		std::cout << "读帧失败" << std::endl;
		return;
	}
	std::cout << "结束" << std::endl;
	return;
```

在 OpenCV 3.0.0 上上述代码将会长时间无响应，因为 OpenCV 并未对此做超时限制，相关问题可查看以下 [Issue6053](https://github.com/opencv/opencv/pull/6053/commits/da48061910db0ee78396237bc78d6f2e321ea5eb)

在2016.02后大概是OpenCV3.2.0后 加入了读写超时限制，默认是30s，相关参数可在 `modules/videoio/src/cap_ffmpeg_impl.hpp` 中查询到


# FAQ

x84 调试debug版本时可能会提示找不到 msvcp120d.dll 和 msvcr120d.dll，需要添加添加到 opencv 的 bin目录下

`\opencv\build\x86\vc12\bin`



# 参考资料

1. [解决msvcp120d.dll和msvcr120d.dll缺失](https://blog.csdn.net/qq_17783559/article/details/78988082)
2. [Opencv下载以及环境配置](https://www.jianshu.com/p/3d4c55bf0926)
3. [Visual Studio 2019 配置OpenCV](https://jtxiao.com/main/posts/visual-studio-2019-%E9%85%8D%E7%BD%AEopencv/)
4. [VS2017配置opencv教程（超详细！！！）](https://bbs.1616ai.com/article/853660460874989568.html)
5. [[常用工具] OpenCV获取网络摄像头实时视频流](https://blog.csdn.net/LuohenYJ/article/details/89403227)
6. [opencv学习---VideoCapture 类基础知识](https://blog.csdn.net/u010368556/article/details/79186992)
7. [Image Signal Processing(ISP)-第一章-ISP基础以及Raw的读取显示](https://blog.csdn.net/weixin_42910064/article/details/102454839)