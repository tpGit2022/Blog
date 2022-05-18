Python 动态类型语言，区分大小写。
Python变量本身没有数据类型，变量存储的值有数据类型。有以下6中基本数据类型
 >

 *  Number 
 *  String
 *  List
 *  Tuple
 *  Dict
 *  Sets

# Number
Number分int,float,bool,complex四种类型。
int整型数值，没有大小的限制。如:`var_int = 11111111`
float 浮点型，带小数的数值。如:`var_float = 1.011111111`
bool 布尔型 只有True和False两种值 。如:`var_bool = True`
complex 复数 只能用j或者J表示不能为其他字母，如: `var_complex = 3+4j`

# String
字符串双引号""或者双单引号''表示,如 `var_str = "string_var"`

# List
列表，中括号表示。例如 `var_list = [1, 1.07, "a", 4-3j]`

# Tuple
元组。小括号表示。例如`var_tuple = (1, 1.06, "a", 3-6j)`

# Dict
字典。大括号表示。例如`var_dict = {"key1": 1, "key2": 1.0, "key3": 1+4j}`

# Sets
集合。大括号表示。例如`var_sets = {"set1", "set2", "set3"}`

# tips
1. 判断变量数据类型的函数。
```
def judge_type(var):
    """
    判断变量存储的数据类型
    :param var: 
    :return: 
    """
    if type(var) == int:
        print("Number type ,is int var")
    elif type(var) == float:
        print("Number type ,is float var")
    elif type(var) == bool:
        print("Number type,is bool")
    elif type(var) == complex:
        print("Number type,is complex")
    elif type(var) == str:
        print("String type")
    elif type(var) == list:
        print("List type")
    elif type(var) == tuple:
        print("Tuple type")
    elif type(var) == dict:
        print("Dict type")
    elif type(var) == set:
        print("Set type")
    else:
        print("unknown type")
```


方法Method和函数Function。

官方定义
Method:` A function which is defined inside a class body. If called as an attribute of an instance of that class, the method will get the instance object as its first argument (which is usually called self)`
Function：`A series of statements which returns some value to a caller. It can also be passed zero or more arguments which may be used in the execution of the body.`


[TOC]

>基于Python3.0。Python2.0和Python3.0的不兼容，差异较大。

国际惯例下来一个HelloPython.
```
#! /usr/bin/python3
print("Hello Python");
```

保存为hello.py。输出：
Hello Python

# 搭建简单的Python3.0运行环境。
* Sublime Text3
* Python的安装包。

# Python基础语法
1. 文件格式编码
    Python3.0的源文件以UTF-8编码，所有字符串为unicode字符串。
2. 标识符
    * 第一个字符必须是字母表或者下划线
    * 标识符其他部分由数字，字母下划线组成
    * Python区分大小写。
3. 保留字
可以运行下面的脚本printkeepword.py得到保留字
```
#! /usr/bin/python3
import keyword
print(keyword.kwlist)
```
运行结果
```
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

4. 注释
单行注释 # 
多行注释 python3.0支持三个单引号进行注释,例如:
```
#! /usr/bin/python3
import keyword
print(keyword.kwlist)
'''
我是多行注释
我是多行注释
我是多行注释
'''

```

5. 行语缩进。
***Python使用缩进来表示代码快***  
注意：缩进的空格数是可变的但同一个代码块的语句必须包含相同的缩进空格数。例如
```
# 正确的缩进
if True:
    print("True")
else:
    print("False")
# 错误的缩进
if True:
    print("Yes")
    print("True")
else:
    print("NO")
  print("False") # 错误的缩进，导致运行错误
```

# 多行语句
通常Python一行一条语句(如果同一行表示多条语句需要用分号;分隔)，如果语句很长可用反斜杠\实现多行语句
```
#! /usr/bin/python3
item_one = 1
item_twp = 2
item_three = 3
item_four = 4
total = item_one +\
    item_twp +\
    item_three +\
    item_four
print(total)

```
注意在[],{},()中的多行语句不需要使用反斜杠。
```
#! /usr/bin/python3
totalNum = {'one', 'two'
            'three', 'four'}
print(totalNum)

```

# 数据类型
Python中的变量不需要声明。但是每个变量使用前必须赋值，因为变量只有被赋值后该变量才会被创建，
**注意：** 在Python中变量就是变量没有类型，我们所说的类型是变量所指的内存对象的类型，等号(=)是用来给变量赋值的，要想删除某个变量可以使用del，删除某个变量后继续调用它会导致运行错误。
```
# ===============基本数据类型================
a,b,c,d,e=20,5.5,True,4+3j,99999999999999999999999999999999999999999999999999999999999
print(type(a),type(b),type(c),type(d),type(e))
print(a+e)
# del c
print(c)
print("=====================================")
count=100 # 整型变量
miles=1000.2 # 浮点型变量
name="hello world" # 字符串
name2='hello world' #字符串
print(count)
print(miles)
print(name)
print(name2)
# 变量的赋值
a=b=c=3
aa,bb,cc,dd=10,10.2,'fdfd',"fdsfdsf"
print(aa,bb,cc,dd)
del name2 # 删除变量name2，后续调用name2将导致错误
del name,miles # 删除多个变量
```
***注意*** type和isinstance的区别在于type认为子类和父类是不同类型，而isinstance认为子类和父类是同一种类型。
python中数有四种类型：整数，长整数，浮点数和复数。
 * 整数 如2
 * 长整数 比较大的整数
 * 浮点数 1.23 ，3E-2
 * 复数 如1+2j
 
### 基本运算
```
>>>5 + 4  # 加法
9
>>> 4.3 - 2 # 减法
2.3
>>> 3 * 7  # 乘法
21
>>> 2 / 4  # 除法，得到一个浮点数
0.5
>>> 2 // 4 # 除法，得到一个整数
0
>>> 17 % 3 # 取余 
2
>>> 2 ** 5 # 乘方
32
```

> Python还支持复数，复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型


## 字符串
* Python中的单引号和双引号使用完全相同
* 使用三引号制定一个多行字符串，例子
```
#! /usr/bin/python3
ta = """fdsfsdfsdfdsfd
sfds"""
print(ta)
# 以下是错误写法 会导致运行错误
ta="fdsfdsfsd
fdsfsdf"
print(ta)
```
* 转义符 \
* 自然字符串，在字符串前加r或者R，如r"this is a line with \n",有前面的r的存在，不会表示换行
* python允许处理unicode字符串，加前缀u或U， 如 u"this is an unicode string"。
* 字符串不可变
* 按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。

# 空格

函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
**记住：** 空行也是程序代码的一部分。

# 同行显示多条语句
Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：
# 多个语句构成代码组
缩进相同的一组语句构成一个代码块，我们称之代码组。
像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
我们将首行及后面的代码组称为一个子句(clause)。
如下实例：
```
if expression : 
   suite
elif expression : 
   suite 
else : 
   suite
```

# import与from ... import
在Python中使用import或者from...import来导入相应的模块。
* 导入整个模块 import somemodule
* 导入某个模块的某个函数 from somemodule import somefunction
* 导入某个模块的多个函数 from somemodule import somefunction1,somefunction2
* 导入某个模块的所有函数 from somemodule import *

# 标准的数据类型
Python3有六个标准的数据类型
* Number(数字)
* String(字符串)
* List(列表)
* Tuple(元组)
* Sets(集合)
* Dictionary(字典)

## Number(数字)
Python2支持int，float，bool，complex。
> Python3没有Python2中的Long，

 * 整型
 * 浮点型
 * 布尔值
 * 复数
例子

## String(字符串)
单引号或者双引号表示
## List(列表)
中括号表示[]
## Tuple(元组)
圆括号表示()
## Sets(集合)
大括号表示{}
## Dictinary(字典)

对比：

| 比较点\类型 | List | Tuple | Sets | Dictionnary |
|:--:|:--:|:--:|:--:|:--:|
| 定义 | 方括号[] | 小括号() | 大括号{} | 大括号{} |
|　例子 | `list=[1,2,3]` | `tup=(1,2,3)` | `stu={1,2,3}` | `dict={};dict[2]=1;` |
| 元素类型 | 类型可不同 | 类型可不同 | 类型可不同 | 类型可不同 |
| 元素可变 | 元素可改变 | 元素不可变 | | 元素可变
| 互异性 | 可重复 | 可重复 | 不可重复 | 可重复 |
| 顺序 | 有序 | 有序 | 无序 | 无序 |


```
if __name__ == '__main__':
    login()
```