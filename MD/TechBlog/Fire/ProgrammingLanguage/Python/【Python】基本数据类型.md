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