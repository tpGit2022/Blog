文件目录的操作需要借助了`os`库，导入该库`import os`
常用方法和说明.

| 方法名 | 方法作用 | 参数说明 | 返回值说明 |
|:---|:--|:--|:--|
| os.getcwd() | 获取运行脚本的目录(***是运行脚本的目录不是脚本本身所在的目录***) | 无参数 | 返回运行脚本的目录 |
| os.listdir(path) | 列出指定目录的内容 | 路径 | 该路径下的文件及目录 |
| os.mkdir(path)  |
| os.rmdir(path)  |
| os.path.isdir(path)  |
| os.path.isfile(path) | 
| os.chdir(path) |

代码实例：
```
#! /usr/bin/python3
# encoding = utf-8
import os
"""
Python3文件管理
"""
script_run_path = os.getcwd()
print("脚本运行的路径为：%d", script_run_path)
var_file_path = "C:/Users/Administrator/Desktop/20170928/temp"
file_list = os.listdir(var_file_path)
for i in file_list:
    print(i)
os.path.isdir()

```