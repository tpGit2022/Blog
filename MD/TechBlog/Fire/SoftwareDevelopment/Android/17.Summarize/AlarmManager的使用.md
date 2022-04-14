使用AlarmManager实现定时任务不受app本身运行状态的影响，是系统时间变化然后产生回调，。只是在各个版本中存在一些差异，
需要区分三种情况
1. API<19
2. 19<=API<23
3. API>=23

# 参考资料
1. [ AlarmManager的使用以及该注意的一些坑](http://blog.csdn.net/WDYShowTime/article/details/73496876)
2. [关于使用AlarmManager的注意事项](http://blog.csdn.net/mazhidong/article/details/71170626)
3. 