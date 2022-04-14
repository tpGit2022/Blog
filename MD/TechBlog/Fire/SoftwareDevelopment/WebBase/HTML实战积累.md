# DIV

设置div大小,颜色,背景
```
<!DOCTYPE html>
<html>
<head>
<meta charset = "utf-8">
<title>Div Style</title>
<style>
.divcss5{width:100px; height:100px; background:#000; color:#FFF} 
</style>
</head>
<body>
<div class="divcss5">100*100</div>
</body>
</html>
```

为标签设置点击事件
```
<!DOCTYPE html>
<html>
<head>
<meta charset = "utf-8">
<title>Strongene</title>
<style>
.divcss5{width:100px; height:100px; background:#000; color:#FFF} 
</style>
<script>
function getCanvasPos() {
      var canvas = document.getElementById("iddiv");
      var pos = canvas.getBoundingClientRect();
      console.log("pos = " + pos.top + " " + pos.right + " " + pos.bottom + " " + pos.left);
      android.getWebViewCanvasPos(pos.left + ";" + pos.top + ";" + pos.right + ";" + pos.bottom );
}
document.getElementById("clickme").onclick = getCanvasPos();
</script>
</head>
<body>
<div id = "iddiv" class="divcss5">100*100</div>
</body>
</html>
```


HTML中以px作为计量单位，而Android中一般以dp和sp作为计量单位，实际中WebView加载的网页会根据dp来处理，如果加载的网页中有100*100的div元素，加载到Android的WebView控件中实际是100dp*100dp，而并非100px。

## 页面加载完毕执行特定方法
```
window.onload=function(){
      //do something
}
// or 
document.getElementById("imgID").onload=function(){
     //do something
}
```

# 选取元素，输出元素属性

  Chrome等浏览器的Web调试工具的控制台key执行一定的js代码，如下点便可获取列表中a
标签的title属性：
```
var list = document.querySelectorAll("#ct > div.mn > div > ul.buddy.cl > li")
list.forEach(v=>{  
    var ea = v.querySelector("h4 > a")
    console.log(ea.title)
});
```

element.innerHTML:获取元素的内容
element.attrName: 获取元素属性名为attrName的值
element.textContent: 获取元素的文本内容