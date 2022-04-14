目前的项目基于SVN，想要SVN，Git同时管理需要进行两大步操作。

1.  由一人收集最新代码，统一提交至Git服务器。
2.  其他人在原来SVN项目目录下初始化本地Git仓库，关联远程仓库，拉取解决冲突。

#  第一步

先说步骤一 代码提交；
收集最新代码后，先在Gitblit服务器上登录个人账号，新建Git仓库，记下仓库地址如：
`ssh://tyw@192.168.41.202:29418/Android/GitTest.git`  

假定收集的代码在`F:\gitgit\Authentication`下，先将其初始化为git仓库，右键Git create repository here..,保存如下代码为newGitignore.sh。  

```
#! /bin/bash
echo 'start to deal!!!'
ls -aR | grep '.svn:' > tmp
sed -n '/\/.svn:/p' tmp | sed 's/\/.svn:/\/.svn\/*/g' > aftertmp
sed -n '/\.\//p' aftertmp | sed 's/\.\//\//g' > .gitignore
# delete tmp files
rm -rf tmp
rm -rf aftertmp 
# add android useless file
echo '/bin' >> .gitignore
echo '/gen' >> .gitignore
echo '/.settings' >> .gitignore
echo 'script is done,all work complete'

```

> 脚本功能主要用于完成排除svn，使得svn相关目录不纳入git管理范围。该脚本需要在项目的根目录下运行。

双击运行newGitignore.sh脚本生成git需要的忽略文件列表文件.gitignore。  

返回上一级目录`F:\gitgit`,选中`Authentication`右键先add 再commit master，完成本地仓库的提交。同样右键`Authentication`,TortoiseGit-Settings-Git-Remote.URL一栏填入远程仓库地址`ssh://tyw@192.168.41.202:29418/Android/GitTest.git`，点击应用，建立本地仓库和远程仓库的连接。接下来开始同步代码。
先拉取重建
![20170803093028.png](../../../Pictures\20170803\20170803093028.png)  
再进行push操作，推送本地代码至git服务器。

# 第二步  

先由一人提交代码至git服务器。其他人同样是先建立本地仓库-排除svn目录-本地add和commit-关联远程仓库。最后只在Fetch & Rebase时可能出现冲突，  
![20170803093623.png](../../../Pictures\20170803\20170803093623.png)  
，手动解决完冲突后，点击commit。之后便是正常的git的pull，push操作了 。