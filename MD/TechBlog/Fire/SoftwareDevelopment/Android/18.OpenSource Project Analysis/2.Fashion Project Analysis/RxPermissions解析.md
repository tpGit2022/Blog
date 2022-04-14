RxPermissions
项目地址:https://github.com/tbruyelle/RxPermissions
RxPermissions用于解决Android6.0之后新增的动态授权问题，实现一句话实现动态授权。
说到动态授权跑不掉以下几个方法：
1. `int checkSelfPermission(String Permissions)`:用于检测是否具备某项权限
2. `void requestPermissions(String[] permissions, int requestCode)`:用于请求某项权限，该函数没有返回值一般和下面的`onRequestPermissionsResult`连用用于接收权限操作的结果
3. `void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults)`:请求权限的结果，一般复写Activity或者Fragment的该方法用于获取请求授权后的具体值决定进行下一步的流程。
4. `boolean shouldShowRequestPermissionRationale(String permission)`:用于判断上一次授权时是否勾选了不再提醒，

一个正常完成的授权流程如下图：
![20180109105022.png](../../../../../Pictures\20180109\20180109105022.png)  

> 

RxPermissions通过动态生成一个Fragment，在Fragment中获取请求授权时的返回值的。