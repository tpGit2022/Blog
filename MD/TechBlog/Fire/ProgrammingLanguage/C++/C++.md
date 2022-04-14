[TOC]


C++

构造函数

构造函数是类的一部分，构造函数和类名一致，没有返回值(不返回类型和Void)，可以初始化成员变量

```

```


宏

`#define alias actual_value`

宏可以嵌套，宏比较长的时候利用反斜杠 `\` 进行换行


MessageBox 是一个宏定义，具体函数原型是

```
 int MessageBox( HWND hWnd, LPCTSTR lpText, LPCSTR lpCaption,UINT uStyle );
```

消息框函数有4 个参数:
hwnd: 父窗口的句柄,为NULL,说明消息框没有父窗口，大多数情况下可以省略不写
lpText: 指向要显示字符串的指针,对话框上显示的信息
lpCaption: 消息框的标题,即提示框上部分显示的内容
uStyle: 消息框的内容和形为(即该消息框有几个按钮、文本对齐等状态，可以在20多个属性值中进行组合)


2.类型常量
　对话框的类型常量可由按钮组合、缺省按钮、显示图标、运行模式四种常量组合而成。
　（1）按钮组合常量


　（2）缺省按钮常量

　（3）图标常量

　（4）运行模式常量

　3.函数返回值

4.示例


https://blog.csdn.net/zollll/article/details/54862128



https://www.cnblogs.com/weiqubo/archive/2010/12/20/1911738.html

# 进制转化

```
#include <iostream>
#include <sstream>
#include <string>
#include <iomanip>
using namespace std;

string dec2hex(int i) {
	stringstream ioss;
	string data_length_hex;
	ioss << setiosflags(ios::uppercase) << hex << i;
	ioss >> data_length_hex;
}
```


# 数据类型

char char* string char[] int unsign int 


bit, byte, word, dword, qword

bit  位即一位二进制数
byte 字节即八位


copydllandrsswtest.bat $(SolutionDir) $(ProjectName)


获取并弹窗显示上一次的错误

```
CString str1;
LPVOID lpMsgBuf;
		FormatMessage(
			FORMAT_MESSAGE_ALLOCATE_BUFFER |
			FORMAT_MESSAGE_FROM_SYSTEM |
			FORMAT_MESSAGE_IGNORE_INSERTS,
			NULL,
			GetLastError(),
			MAKELANGID(LANG_NEUTRAL, SUBLANG_DEFAULT),
			(LPTSTR)&lpMsgBuf,
			0,
			NULL
		);
		str1.Format(L"错误码 errorCode=%d", GetLastError());
		ShowColorLog(str1, 255, 0, 0);
		MessageBox(NULL, (LPCTSTR)lpMsgBuf, L"Error", MB_OK | MB_ICONINFORMATION);

		LocalFree(lpMsgBuf);
```


# Hex2ASCII



```

#include <iostream>
#include "abstract.h"

int get_dec(char c);

int main(int argc, char* argv[])
{
	// i = 0 代表的exe本身
	for (short i = 1; i < argc; i++) {
		unsigned int most = get_dec(argv[i][0]);
		unsigned int last = get_dec(argv[i][1]);
		unsigned int index = (most * 16) + last;

		printf("%c", index);
	}
	return 0;
}


int get_dec(char c) {
	if (c >= '0' && c <= '9') {
		return c - '0';
	}
	if (c >= 'a' && c <= 'z') {
		return c - 'a' + 10;
	}
	if (c >= 'A' && c <= 'Z') {
		return c - 'A' + 10;
	}
	return 0;
}
```


# strcpy_s函数


strcpy_s 包含在 `<string.h` 中定义如下:


```
_ACRTIMP errno_t __cdecl strcpy_s(
        _Out_writes_z_(_SizeInBytes) char*       _Destination,
        _In_                         rsize_t     _SizeInBytes,
        _In_z_                       char const* _Source
        );

```

第一个参数：最终被赋值的字符串指针
第二个参数：要拷贝的字节数，可以通过 `strlen()` 方法求出，因为索引从零开始 记住加1
第三个参数：被复制的字符串指针


C++ 进制表示

```
int a = 2323; // 十进制
int b = 0b1001010101; //二进制
int c = 0xFA; //十六进制
int d = 023; //八进制
```


CString 的头文件

非MFC程序中是 `<atlstr.h>`  MFC程序中 `<afxstr.h>`


# 错误集合

1. 数组定义常量长度导致数组越界

```

```

不确定的数组长度，需要使用动态分配的方式

memset 用于内存的分配，可用于类，结构体中，譬如

```
				tm *ptrTime;
				memset(&ptrTime, 0, sizeof(tm*));
```


文件，文件夹IO操作


保存为BMP


```


void SaveBitmap(uint8_t *data, int width, int height, int bpp)
{
	BITMAPFILEHEADER bmpHeader = { 0 };
	bmpHeader.bfType = ('M' << 8) | 'B';
	bmpHeader.bfReserved1 = 0;
	bmpHeader.bfReserved2 = 0;
	bmpHeader.bfOffBits = sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER);
	bmpHeader.bfSize = bmpHeader.bfOffBits + width * height*bpp / 8;

	BITMAPINFO bmpInfo = { 0 };
	bmpInfo.bmiHeader.biSize = sizeof(BITMAPINFOHEADER);
	bmpInfo.bmiHeader.biWidth = width;
	bmpInfo.bmiHeader.biHeight = -height;  // 反转图片
	bmpInfo.bmiHeader.biPlanes = 1;
	bmpInfo.bmiHeader.biBitCount = bpp;
	bmpInfo.bmiHeader.biCompression = 0;
	bmpInfo.bmiHeader.biSizeImage = 0;
	bmpInfo.bmiHeader.biXPelsPerMeter = 100;
	bmpInfo.bmiHeader.biYPelsPerMeter = 100;
	bmpInfo.bmiHeader.biClrUsed = 0;
	bmpInfo.bmiHeader.biClrImportant = 0;

	// 打开文件
	std::ofstream fout("2022_03_21_16.bmp", std::ofstream::out | std::ofstream::binary);
	if (!fout)
	{
		return;
	}
	// 使用结束后关闭
	std::shared_ptr<std::ofstream> foutCloser(&fout, [](std::ofstream *f) { f->close(); });

	fout.write(reinterpret_cast<const char*>(&bmpHeader), sizeof(BITMAPFILEHEADER));
	fout.write(reinterpret_cast<const char*>(&bmpInfo.bmiHeader), sizeof(BITMAPINFOHEADER));
	fout.write(reinterpret_cast<const char*>(data), width * height * bpp / 8);
}

```


获取时间

```
	time_t nowtime;
	//首先创建一个time_t 类型的变量nowtime
	struct tm* p;
	//然后创建一个新时间结构体指针 p 
	time(&nowtime);
	//使用该函数就可得到当前系统时间，使用该函数需要将传入time_t类型变量nowtime的地址值。
	p = localtime(&nowtime);
	//由于此时变量nowtime中的系统时间值为日历时间，我们需要调用本地时间函数p=localtime（time_t* nowtime）将nowtime变量中的日历时间转化为本地时间，存入到指针为p的时间结构体中。不改的话，可以参照注意事项手动改。
	printf("%d_%02d_%02d_%02d_%02d_%02d\n", p->tm_year + 1900, p->tm_mon + 1,p->tm_mday, p->tm_hour, p->tm_min, p->tm_sec);



	或者

	time_t timep;
    	time(&timep);
    	char tmp[256];
    	strftime(tmp, sizeof(tmp), "%Y-%m-%d %H:%M:%S", localtime(&timep));
    	cout << tmp << endl;


    	// 上述时间精度不够
    	#include <windows.h>
    	SYSTEMTIME sys;
	GetLocalTime(&sys);
	printf("%4d_%02d_%02d_%02d_%02d_%02d_%03d", sys.wYear, sys.wMonth, sys.wDay, sys.wHour, sys.wMinute, 
		sys.wSecond, sys.wMilliseconds);
```


格式化字符串

```
	time_t timep;
	time(&timep);
	char tmp[256];
	strftime(tmp, sizeof(tmp), "%Y_%m_%d_%H_%M_%S", localtime(&timep));
	char out_file[MAX_PATH] = { 0 };
	printf("\n保存当前帧为:RTSP_%s.JPG\n", tmp);
	sprintf_s(out_file, sizeof(out_file), "JPEG/RTSP_%s.JPG", tmp);
```


MFC 下的 CString 转 int

```
CString Temp("8");

int ComNum = _ttoi(Temp);  
```


关键字 `#ifdef, ifndef, endif`

条件编译，为了处理头文件被多个cpp文件所引用导致的编译出现重复定义错误，语法 


```
#ifndef __UITLS__
#define __UITLS__
.....
/// you define code
.....
#endif
```

MFC下的CString，格式化字符串, 格式化字符串的格式 `%[标志][输出最小宽度][精度]<转化说明符>` 转化说明符常见类型如下:  

| 格式 | 代表含义 |
|:--|:--|
| %c | 单个字符 |
| %d | 十进制输出(int) |
| %ld | 十进制输出(long) |
| %f | 十进制输出浮点数(float) |
| %lf | 十进制输出浮点数(double) |
| %o | 八进制数 |
| %s | 字符串 |
| %u | 无符号数十进制 |
| %x | 十六进制数 |

> %x 输出小写十六进制 %X 输出大写十六进制

标志有 `-,+` 两种 `-` 代表左对齐 右侧补空  `+`   代表右对齐 左侧补空

输出最小宽度 十进制表示

精度 以 `.` 开始，后面跟一个十进制数 ，当输出数字时表示小数的位数，输出字符时表示输出的字符个数



# 动态加载DLL

静态调用需要 `dll, lib,.h` 三个文件，`lib, .h` 是调用方需要的文件

动态调用 只需要 `dll` 但是 调用放需要知道相关函数的返回值类型和传入参数类型

* 编写DLL

VS2017 

```cplusplus

//framework.h
#pragma once

#define WIN32_LEAN_AND_MEAN             // 从 Windows 头文件中排除极少使用的内容
// Windows 头文件
#include <windows.h>

extern "C" __declspec(dllexport) int Add(int *a, int *b);


//framework.cpp
#include "pch.h"

#include <stdio.h>

int Add(int * a, int * b)
{
	printf("开始执行DLL中的 Add函数");
	return *a + *b;
}

```

* 调用DLL

调用流程
1. 定义函数指针返回值类型和形参类型必须完全一致
2. 通过 `Windows.h`中的 LoadLibrary 加载dll
3. 通过 `GetProcAddress` 获取到函数所在的地址
4. 通过函数指针调用dll中的函数
5. 释放dll

```cplusplus
#include <iostream>
#include <Windows.h>

int main()
{
	std::cout << "动态调用DLL" << std::endl;
	HINSTANCE hDllInst = LoadLibrary(L"..//DLL//x86//DllTest.dll");
	if (hDllInst) {
		std::cout << "\n动态加载DLL成功" << std::endl;
		//typedef int(WINAPI *Add)(int, int);
		typedef int(WINAPI *Add)(int*, int*);
		Add funAdd = NULL;
		funAdd = (Add)GetProcAddress(hDllInst, "Add");
		if (funAdd) {
			std::cout << "获取到了函数指针地址" << std::endl;
			int num1 = 3, num2 = 4;
			int sum = funAdd(&num1, &num2);
			std::cout << "DLL计算的结果:" << sum << std::endl;
		}
		std::cout << "\n准备释放DLL" << std::endl;
		FreeLibrary(hDllInst);
	}
}


```