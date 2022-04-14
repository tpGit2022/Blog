Java题库-基础题答案.md

1. 抽象类

2. switch(var)中的var的类型
`var`的类型可以是除开`boolean`以外的基本类型(byte,short,int,char,float,double)
`var`根据JDK的版本有所不同，

3. char型变量是否可用存储一个中文汉字？
可以，任何存在于Unicode编码字符集以下的汉字都可以用char类型的变量存储，一个汉字占据两个字节的存储空间，

4. 基本类型占据的字节数。

byte 1      short 1     int     2
char 2      float 2     double 4
根据JVM的规范基本类型占据的字节数是固定的
