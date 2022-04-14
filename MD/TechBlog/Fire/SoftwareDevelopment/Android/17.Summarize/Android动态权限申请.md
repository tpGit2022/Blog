shouldShowRequestPermissionRationale 该方法用于是否需要显示权限申请的具体说明,只在一种情况下为True，当用户拒绝了一次授权并且尚未勾选时该方法返回为True，其他情况:第一次安装时调用该方法为False，用户拒绝了授权并且勾选了不再提醒调用该方法返回False.


`targetSdkVersion 23`  23即Android6.0,Android系统开始新增权限处理的版本，若不想做动态权限的申请则最高的`targetSdkVersion`只能为22，`targetSdkVersion`为23及以上必须做动态权限的申请，否则会发生错误。

一个完整的授权流程如下;
1. 判断app当前是否有需要的权限
2. 如果没有调用授权方法开启授权
3. 根据授权返回值成功，不成功调用是否该显示授权具体提示方法
4. True显示为何需要权限调用授权方法，False显示为何需要权限跳转至app权限设置界面
5. 