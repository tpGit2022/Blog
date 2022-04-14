git下载地址
https://git-for-windows.github.io/
乌龟壳Git(TortoiseGit)下载地址
https://download.tortoisegit.org/tgit/2.5.0.0/
一般会切换至`~/.ssh`目录下再执行命令。
添加ssh
`ssh-keygen -t rsa -C "youremailaddress"`

指定生成的文件名
`ssh-keygen -t rsa -C "youremailaddress" -f filename`

ssh -T git@github.com

关联远程仓库

`git remote add ogigin git@github.com:yourgithubusername/yourgitresponame.git`  
首次关联的后续操作  
由于远程仓库可能不为空先拉取仓库中的内容到本地。
`git pull origin master`

http://www.jinbuguo.com/openssh/ssh-keygen.html



