> svn版本
  >> svn, version 1.9.4 (r1740329)
   compiled Aug  3 2016, 17:00:22 on x86/x86_64-microsoft-windows6.1.7601


# 命令用法一览
usage: svn <subcommand> [options] [args]  
Subversion command-line client.  
Type 'svn help <subcommand>' for help on a specific subcommand.  
Type 'svn --version' to see the program version and RA modules
or 'svn --version --quiet' to see just the version number.

Most subcommands take file and/or directory arguments, recursing
on the directories.  If no arguments are supplied to such a
command, it recurses on the current directory (inclusive) by default.

## 用法翻译
 用法： svn <子命令> [可选项] [参数]
 > 注 一般<>代表必备参数 []是可选的不加的项目


# 子命令
```
Available subcommands:
   add
   auth
   blame (praise, annotate, ann)
   cat
   changelist (cl)
   checkout (co)
   cleanup
   commit (ci)
   copy (cp)
   delete (del, remove, rm)
   diff (di)
   export
   help (?, h)
   import
   info
   list (ls)
   lock
   log
   merge
   mergeinfo
   mkdir
   move (mv, rename, ren)
   patch
   propdel (pdel, pd)
   propedit (pedit, pe)
   propget (pget, pg)
   proplist (plist, pl)
   propset (pset, ps)
   relocate
   resolve
   resolved
   revert
   status (stat, st)
   switch (sw)
   unlock
   update (up)
   upgrade
```

Subversion is a tool for version control.
For additional information, see http://subversion.apache.org/
