

  Linux 环境变量PATH(注意大小写),新增环境变量可以从几个地方入手，
1. 修改/etc/profile 
  在文件末尾加上 `export PATH=$PATH:yourPath`,所有用户有效
2. 修改单一用户的 `.bash_profile`
   在文件末尾加上 `export PATH=$PATH:yourPath`，只有当前用户有效
3. 终端执行 `export PATH=$PATH:yourPath`
  只有该终端和该终端的子终端有效
显示PATH的值 `echo $PATH`