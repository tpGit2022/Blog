EditText是TextView的直接子类，常用于信息的输入。

1. 实现密码的显示和隐藏。
```
            //设置为密码可见
            etPassword.setTransformationMethod(HideReturnsTransformationMethod.getInstance());
            //设置为密码不可见
            etPassword.setTransformationMethod(PasswordTransformationMethod.getInstance());
```

上述代码存在一个小问题，切换密码的可见不可见时输入光标会被重置。通过EditText的setSelection方法定位输入光标位置.
```
etPassword.setSelection(etPassword.getText().toString().length());
```

2. 