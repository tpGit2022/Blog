# 透明背景，点击穿透
1. 发生时间:`2017-09-10 10:00:00`  耗时:`xxdxxhxxm`
2. 问题标签 `muldex`,`nullpoint`
3. 问题具体描述
4. 错误日志
***日志代码：***
```

```
5. 原因分析

6. 解决方案
透明背景层添加属性
`android:clickable="true"`
或者透明层的控件复写或者设置监听器事件分发方法，返回true,禁止事件进一步分发
```
mView.setOnTouchListener(new View.OnTouchListener() {
    @Override
    public boolean onTouch(View arg0, MotionEvent arg1) {
        return true;
    }
});
```
***解决方案代码:***
```

//
```
7. 参考资料
8. 反思和总结