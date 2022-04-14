
开启js支持
`webView.getSettings().setJavaScriptEnabled(true);`

Java执行JavaScript方法

```
 webView.loadUrl("javascript:javascriptmethodname(args)");  
```

> 执行格式 javascript:js方法

JavaScript执行Java方法

1. Java层定义包含`@JavascriptInterface`注解的方法，web设置JavascriptInterface

```
webView.addJavascriptInterface(new WebJsInterface(this), "android");
public class WebJsInterface {
    @JavascriptInterface
        public void testJsCallback() {
            touchHelper.setRawDrawingEnabled(false);
            Toast.makeText(mContext, "Quit Pen from WebView", Toast.LENGTH_SHORT).show();
    }
}

```

> addJavascriptInterface(Object object, String name)
> object 为包含`@JavascriptInterface`方法的类，name是别名将会在JavaScript中用到


2. 在js中通过name调用Java的方法。
```
function getCanvasPos() {
      var canvas = document.getElementById("myCanvas");
      var pos = canvas.getBoundingClientRect();
      android.testJsCallback();
}
```


# 参考资料
1. [Android：你要的WebView与 JS 交互方式 都在这里了](https://blog.csdn.net/carson_ho/article/details/64904691)
2. [Android WebView —— Java 与 JavaScript 交互总结](https://yifeng.studio/2016/12/01/android-webview-java-js-interaction/)