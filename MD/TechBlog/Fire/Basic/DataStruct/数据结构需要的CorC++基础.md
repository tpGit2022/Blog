C++中的判断和Java不同。比如说 

```
Java:
while(n !=0) {
    ....
}

C++
while(n) {
    ....
}
```

C++ 中的条件只有 `n == 0` 为 false，其他情况均为true


关键字`typedef`,类型定义，用于用自己起的名称的类型代替已有的类型，如：
```
type int CustomType;
CustomType i;//相当于int i
```

`typedef`常与`struct`关键字连用。
结构体命名：
```
typedef char ElemType;
typedef struct QNode 
{
    ElemType data;
    struct QNode *next;
} QType;
```

> `QType`代表的`struct QNode`

一般结构体的定义方式有三种：
```

```

```
SqList *&L
SqList *L
```

# 参考资料
1. [c++ 中的各种进制转换函数整理](https://blog.csdn.net/wangjunchengno2/article/details/78690248)