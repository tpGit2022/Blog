[TOC]


https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository  

https://git-scm.com/docs/gitignore

注意 ! 的配置效果

! 用于不忽略某个文件，例如如下

```
*.txt
!/aaa/ccc/4.txt
```

上述配置会让 git 忽略掉除 /aaa/ccc/4.txt 之外所有的txt文件。

需要注意的是 如果 之前排除了 aaa或者ccc目录，再加上 ! 的配置是无效的，也就是4.txt依旧会被忽略掉

```
An optional prefix "!" which negates the pattern; any matching file excluded by a previous pattern will become included again. It is not possible to re-include a file if a parent directory of that file is excluded.
```