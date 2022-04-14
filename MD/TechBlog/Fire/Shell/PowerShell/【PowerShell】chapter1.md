PowerShell
Win7 自带PowerShell功能，win+R，键入PowerShell。
PowerShell脚本文件的后缀名为.ps1。
windows系统默认不允许执行PowerShell脚本文件，需要先修改设置。
在PowerShell中执行如下语句
先判断当前系统是否允许执行PowerShell脚本`get-executionpolicy`

> 如果为Restricted表示禁止执行脚本。

执行允许脚本执行的命令`set-executionpolicy -executionpolicy unrestricted`

PowerShell中有个名词叫Cmdlet，Cmdlet是command-let的缩写。它指的可执行的命令如Get-Command,所有的cmdlet均以标准的"动词+名词"命名,输入Get-Command可以获取PowerShell中所有可用的cmdlet，共计410条命令。

PowerShell中可以直接执行数学运算


"ls" 和 &"ls" 的区别：前者将ls当成普通的字符串而后者将执行ls命令。
在PowerShell中可以执行cmd的命令，部分只有cmd拥有的命令可以通过
在PowerShell中通过cmd /c commandname 来执行如执行dir /b
`cmd /c dir /b`


别名 Alias

在Powershell中执行多条命令，；分割

`Get-ExecutionPolicy`