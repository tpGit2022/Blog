BruteForce模式匹配算法简称BF算法，也叫简单匹配算法。
基本思想：
目标串`s[0,...n-1]`和模式串`t[0,...,t-1]`,依次比较`s[i]`和`t[j]`,相等则比较`s[i+1]`和`t[j+1]`,不相等则`s[i+1]`和`t[0]`即只有发生过一次不相等就重新匹配,直至找到相等的位置或已达目标串的终点。

BF模式匹配算法很容易理解，举个例子，目的串s=`aaaaab`和模式串t=`aaab`的BF模式匹配算法的执行过程如下：

1. 第一趟匹配
    i的初值为0，j初值为0
    i=0,j=0 `s[0]=a,t[0]=a`,相等 i++,j++;
    i=1,j=1 `s[1]=a,t[1]=a`,相等 i++,j++;
    i=2,j=2 `s[2]=a,t[2]=a`,相等 i++,j++;
    i=3,j=3 `s[3]=a,t[3]=b`,不相等 i=i的初值0+1,j=0;
2. 第二趟匹配
    i的初值为1，j的初值为0
    i=1,j=0,`s[1]=a,t[0]=a`,相等 i++,j++;
    i=2,j=1,`s[2]=a,t[1]=a`,相等 i++,j++;
    i=3,j=2,`s[3]=a,t[2]=a`,相等 i++,j++;
    i=4,j=0,`s[4]=a,t[3]=b`,不相等 i=i的初值1+1,j=0;
3. 第三趟匹配
    i的初值为2,j的初值为0
    i=2,j=0,`s[2]=a,t[0]=a`,相等 i++,j++;
    i=3,j=1,`s[3]=a,t[1]=a`,相等 i++,j++;
    i=4,j=2,`s[4]=a,t[2]=a`,相等 i++,j++;
    i=5,j=3,`s[5]=b,t[3]=b`,相等 i++,j++;
    此时j已达最大值3，匹配结束。
模式串t匹配目标串s，从目标串中的第i=2个字符开始目标串s依次和模式串中字符相等。

BF算法的C实现
k值用于保存目标串s中每一次匹配的起点。
```
int BruteForce(SqString s,SqString t)
{
    int i=0,j=0,k=0;
    while(i<s.len&&j<t.len)
    {
        if(s.data[i]==t.data[j])
        {
            i++;
            j++;
        }else
        {
            k++;
            i=k;
            j=0;
        }
    }
    if(j==t.len)
        return i-j;
    else
        return (-1);
}
```

当然更常见的是下面的写法即不要变量k直接用`i-j+1`表示匹配的起点。
```
int BruteForce(SqString s,SqString t)
{
    int i=0,j=0;
    while(i<s.len&&j<t.len)
    {
        if(s.data[i]==t.data[j])
        {
            i++;
            j++;
        }else
        {
            i=i-j+1;
            j=0;
        }
    }
    if(j==t.len)
        return i-j;
    else
        return -1;
}
```