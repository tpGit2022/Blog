[TOC]

# 前因

Git 中提交当前目录有变化的文件及目录的操作非常频繁就想着写个集成脚本。

## 需求

执行一条命令即可完成当前目录下有变动的文件及目录的提交，提交信息由用户输入

# 分析

变动的文件有修改的，有删除的，有新增的，明显是标准的先 add 后 commit 的操作。
考虑上 Git 其别名的方式 `git config --global alias.ss status`, 不够灵活，而且执行命令是带有 `git` 前置条件的，只能考虑 Shell 脚本。

脚本的流程应该如下：

1. 检测是否输入了 commit message，没有就中断且提示否则下一步
2. 切换至脚本运行的目录，执行 git add 命令
3. add 成功后执行 git commit -m "message" 命令，add 不成功提示用户且中断
4. 执行 git status, 查看当前目录状况

# 最终方案

保存如下代码为 `gcmt`

> 注意是 gcmt 而非 gcmt.sh

```
#! /bin/bash
<<'COMMENT'
Git 提交脚本，提交当前路径有变动的文件，提交信息由用户输入,用户必须输入提交信息，提交信息用双引号括起来
例如 gcmt "fix(project): fix bug #12013"
注意：commit message 里面的英文双引号将会被移除
COMMENT
# combine git add and git commit -m
# when your set variable，don't leave any blank before or after symbol =
origin_commit_message=$1
new_commit_mesage="'"${origin_commit_message}"'"
# echo "origin_commit_message = $origin_commit_message"
# echo "new_commit_mesage = $new_commit_mesage"

script_store_path=$(cd "$(dirname "$0")";pwd)
script_exec_path=$(pwd)
# echo "store_path="${script_store_path}
# echo "exec_path="${script_exec_path}

if [ -z "${origin_commit_message}" ]; then
    echo "Please input commit message, put commit in double quotation marks"
    exit 2
fi

# exit 3

# swith path
cd "${script_exec_path}"

git add .
if [ $? -eq 0 ]; then
    git commit -m "${new_commit_mesage}"
    if [ $? -eq 0 ]; then
        echo "git commit success"
    else
        echo "git commit error, fix it and retry"
        exit 4
    fi
else
    echo "git add file failed, please resolve error,and retry"
fi
git status .
```


脚本运行的效果如下：

![20190928233357.png](E:\MyBlogs\MD\TechBlog\Pictures\20190928\20190928233357.png)

如果提示权限不足，那就修改下权限 `chmod 755 gcmt`

# 路障

> 途中碰到的一些问题，没啥用。只是为了自己吐槽

途中遇到了很多啼笑皆非的错误，本身对 Shell 熟悉程度一般般很早的时候玩过一点点。

* 多行输入问题

脚本的多行输入中途测试一直有问题，输入双引号后可以直接输入输入了双引号也没啥用单引号同样，一脸懵逼，赶紧测试 ls， git commit 等等指令发现又是正常的，一度以为系统提供的脚本做了特殊处理，后来出去跑个步发现突然正常了。再三验证发现自己脚本终端执行的时候中英文的双引号和单引号混着用了，所以没匹配上导致了可以一直输入

* cygwin的No such file or directory

初期写的 gcmt 脚本中的路径是提供的，比如 add 是 `git add ${script_exec_path}`
结果老是报 `fatal: Invalid path '/cygdrive': No such file or directory`,不知道啥毛病，cygwin 终端磁盘都是 挂载在 `/cygdrive` 目录下，而 git 使用的目录好像和这不一样，一度想过对 cygwin 的终端特别处理，后来发现使用相对路径就好 `git add .` 神清气爽。

# 参考资料
