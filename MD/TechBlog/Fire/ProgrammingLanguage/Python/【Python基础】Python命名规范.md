命名规范的作用对象。

命名规范约束的有：   


***Python之父Guido推荐的规范***

| Type | Public | Internal |
|:--|:--|:--|
| Modules | lower_with_under |  \_lower\_with_under |
| Packages | lower_with_under | 
| Classess | CapWords | _CapWords |
| Exceptions | CapWords |  |
| Functions | lower_with_under() | \_lower\_with_under() |
| Gloal/Class Constants | CAPS_WITH_UNDER | \_CAPS\_WITH_UNDER |
| Global/Class Variables | lower_with_under | \_lower\_withd_under |
| Instance Variables | lower_with_under() | \_lower\_with_under (protected) or \_\_lower_with_under (private) |
| Function/Method Paramemtes | lower_with_under | |
| Local Varivalbe | lower_with_under | |

概括的来讲就是全局变量用全大写，类名和异常用大驼峰命名，其余均用小驼峰命名下划线分割。

下划线 单个下划线代表protected 双下划线代表private

> internal 表示仅模块内可用或者在类中保护或者私有
> 


# 参考资料
1. (Google开源项目风格指南-Python风格规范)[http://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/]


Python3命名规范约束的东西有：
包名 ，模块名 ，类名，函数名/方法名 全局变量/类变量 全局常量/类常量
本地变量 实例变量 ，异常 函数/方法的参数

大部分局势小写下划线分割
全局常量 全部大写下划线分割
类名 大驼峰命名下划线分割即首字母都大写
异常 大驼峰命名下划线分割即首字母大写



| 类型 | 公共 | 内部的 |
|:--|:--|:--|
| 包名 | 小写下划线分割 | |
| 模块名 | 小写下划线分割 | 一个下划线开头小写下划线分割 |
| 类名 | 首字母均大写下划线分割 | 下划线开头首字母大写下划线分割 |
| 异常 | 首字母大写下划线分割 | |
| 全局常量/类常量 | 全部大写下划线分割 | 下划线开头全部大写下划线分割 |
| 函数名/方法名 | 小写下划线分割 | 下划线开头小写下划线分割 |
| 
