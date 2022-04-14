第三部分 学习shell和shellscript


第十一章 认识和学习bash

type命令 用于识别命令是外部命令还是bash的内置命令。比如`type chmod`和`type ls`，前者是bash内置命令而后者是外部命令。

# Shell变量的功能
## 变量
 变量的命名规则：只能是英文字母和数字且不能是数字开头。使用时需要在变量前面加上"$"，
 **变量的设置规则**  
 1. 变量与变量规则以一个等号= 来连接。例如：`myname=varconent`,myname是变量名，而varconent是变量名为myname的变量是内容。
 2. 等号两边不能直接接空格符号。
 3. 变量内容若有空格符号可使用双引号””“或者单引号“’”将变量内存结合起来。但双引号中的特殊字符会保持原有特性而单引号不会。比如vari=content;echo "$vari";显示的是content而vari=content;echo '$vari';显示的是字符串$vari。
 4. 使用转义字符反斜杠"\"可以将特殊字符转换为一般字符。
 5. 可使用反单引号即数字1左侧的符号或者是$(命令)可以表示其他命令的结果，比如var="$(uname) hello dog";echo $var;命令结果显示为Linux hello dog，就是将uname命令的结果作为变量内容的一部分。
 6. 为变量追加内容使用"$变量名称"或者${变量}，例如PATH="$PATH":/home/bin或者PATH=${PATH}:/home/bin;
 7. 若变量需要在子进程中执行使用export命令将变量变成环境变量。
 8. 通过unset关键字取消变量的设置，例子：`unset myvarname`
 9. 变量默认是字符串类型，通过declare -i可将变量设置为整型，
 10. shell中的数组var[1]="fd"，数组类型为保证正确读取建议使用${数组}的方式来读取数据，`echo ${var[1]}` 表示数组var中的下标为1的值即fd
 11. 
" 
**read**  
read用于接受用户键盘的输入，常用参数-p或者-t或者两者皆有，p由于用户输入提示语，而-t表示等待的时间，时间到了则略过该命令。例子(将用户的输入作为变量name的值，若10秒之内未输入则自动跳过read命令执行echo命令)：  
```
 read -p "please input your name:" -t 10 name;echo $name;
```

**declare** 和 **typeset**    ubuntu 16.04 命令行提示typeset已被舍弃(Obsolete).
用于申明变量的类型。`delcare [-aixr] variable`,-a 将变量定义为数组array类型，i将变量定义为整型数组，-x 用法和export一样，将varivale变为环境变量，r将变量设置为只读变量，不可更改不可重设。

**变量值的删除修改**  (path为自定义的变量其值与$PATH值相同)
**删除**  从左至右删除使用 `#` 或者`##`,从右至左使用百分号%或者%%。 `${path#/*:}` ，分为三部分path是一部分代表要处理的变量，以`#`或者`##`为分割其后`/*:` 是第三部分作为匹配的部分，`#`代表只删除从左至右匹配到的第一个，而`##`会删除所有匹配到的字符。
%和%%的意义和#相同只是删除顺序相反。
```
ghost@ghost-pc:~$ echo $path;
/usr/local/android-studio/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/usr/SoftWare/Android/Sdk/platform-tools/:/usr/SoftWare/Android/Sdk/tools/:/usr/local/myshell/
ghost@ghost-pc:~$ echo ${path#*android-studio*:}  
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/usr/SoftWare/Android/Sdk/platform-tools/:/usr/SoftWare/Android/Sdk/tools/:/usr/local/myshell/
ghost@ghost-pc:~$ echo ${path#/*:}
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/usr/SoftWare/Android/Sdk/platform-tools/:/usr/SoftWare/Android/Sdk/tools/:/usr/local/myshell/
ghost@ghost-pc:~$ echo ${path##/*:}
/usr/local/myshell/
ghost@ghost-pc:~$ 
```

