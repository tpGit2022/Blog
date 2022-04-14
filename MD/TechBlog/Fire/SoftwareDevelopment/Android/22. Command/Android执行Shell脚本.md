[TOC]

在 Android 设备上是可以执行 shell 脚本的不过和 Linux 上的脚本不同，开头使用 `#! /system/bin` 而非 `#! /bin/sh`

期望是在终端或者PC端执行 `xxx.sh` 或者 `adb shell xxx.sh` 即可执行相应的 Shell 脚本。

想要不加全路径执行脚本，必定少不了环境变量PATH的支持，想要运行脚本运行的权限x必不可少。

终端重新赋值PATH， `PATH=${PATH}:yourshellstorepath`

最后发现 加了 PATH也没啥鸟用，不知道是不是加的地方不对，执行时也被不能像ls,cd等指令需要 `sh yourshellname` 方可执行，需要指定脚本位置，换句话将在脚本所在目录以外的位置需要指定绝对路径来指定脚本

目前探测的情况得知

红米 HM NOTE 1LTE 的 `/`,`/system` 均处于只读状态。