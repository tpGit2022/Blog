>  本文只对CMD命令的常见用法做出归纳，不做深入探讨


# 常用命令
## 批处理的注释
注释不会被执行，只为了提高批处理脚本的可读性。常见的注释方式有以下三种：
1. rem  表示单行注释。例子如下  
        rem 我是注释
2. goto label 表示段注释，label名称随意。goto的含义跳转label处的代码开始执行。例子如下
```
goto start
	@脚本声明
	@2016/12/5
:start
```
3. echo 可做单行注释且会回显，常作提示语表示进度
        echo "同步新增或者修改的文件"

## 基本命令
1. echo  
显示信息或者设置命令的回显  
  1. 显示信息  
          echo  我是echo的显示信息
  2. 设置命令是否回显 为on将显示执行的命令cd /d E:,为off将直接执行不在屏幕总显示执行的命令
```
@echo off
cd /d E:
```

2. set
3. setlocal
4. if
5. for
6. start
7. cls  
清除屏幕，用于去除屏幕的冗余信息
8. exit
9. more
10. 管道命令重定向
11. pause

## 时间日期命令time,date
1. time
2. date

## 文件及目录操作管理
1. type
2. mkdir md
3. rmdir rd
4. copy xcopy
5. cd chdir
6. dir
7. del erase
8. ren rename
9. move
10. tree

## 搜索
1. find
2. findstr

## 任务管理
1. tasklist
2. taskkill

## 批处理的参数

## 其他乱七八糟的东西

# 常见变量声明
  ## 当前用户的目录
  `%USERPROFILE%`

# 常用命令模块

## 获取当前盘符，当前绝对路径及各种路径相关

## 创建日期时间相关的文件夹
