
Git 子模块(submodule)。

当前项目git项目 `project`, 里面子目录 `submodule`, 现在需要将 `submodule` 单独出来作为git项目 `subproject`。

1. 抽取信息到新分支
```
git subtree split -P dir_name -b new_branch_name
```

> dir_name 是 project 下的子目录  
> new_branch_name 新分支名称  
> dir_name 相关的提交信息会被抽取到分支 new_branch_name

2. 推送新分支到新仓库

```
cd ..
mkdir subproject
cd subproject
git init
git pull ../project new_branch_name
```

相关命令:

```
git submodule update --init --recursive
git submodule foreach `<command>`
```

# 参考资料
1. [如何把GIT仓库的子目录独立成新仓库](https://blog.csdn.net/lujun9972/article/details/46944733)
2. [6 Git 工具 - 子模块](https://git-scm.com/book/zh/v1/Git-%E5%B7%A5%E5%85%B7-%E5%AD%90%E6%A8%A1%E5%9D%97)