对符合条件的元素进一步正则匹配  

```
var selector = "#main > div:nth-child(4) > table > tbody > tr.tr1.do_not_catch > th:nth-child(2) > table > tbody > tr > td > div:nth-child(9)";
var list = document.querySelectorAll(selector)
var reg = /[0-9a-fA-F*_?.$#@'@#￥*？，。Xx]{16,30}/g
list.forEach(k=>{
    var array = [...k.innerText.matchAll(reg)]
    array.forEach(v=>{
    console.log(v)
    console.log(v[0])
    });
});
```

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/matchAll  

matchAll 方法返回 iterator  
正则中的 g 表示全局匹配即即便匹配到了已经匹配直至字符串全部匹配完  
如果没有该项 matcherAll 只会返回符合条件的第一项

查询符合条件的元素并遍历输出

```
var selector = "#ct > div.mn > div > ul.buddy.cl > li";
var list = document.querySelectorAll(selector)
list.forEach(v=>{  
    console.log(v)
});
console.log(list.length)
```

测试正则表达式

```
var reg = /[0-9]+/
var input = 289
var flag = reg.test(input)
console.log(flag)
```

```
/\$/.test("$")                        //js match $
"$".matches("\\$")                    //java match $
/\\/.test("\\")                       //js match \
"\\".matches("\\\\")                  //java match \
/\\\\/.test("\\\\")                   //js match \\
"\\\\".matches("\\\\\\\\")            // java match \\
```

> reg 中的 // 表示两个斜杠中间的是正则表达式

删除节点。

```
var node = document.getElementById("wrapper");
node.parentNode.removeChild(node);
```

leetcode 移除非会员不能查看的问题：

```
var selector = "#question-app > div > div:nth-child(2) > div.question-list-base > div.table-responsive.question-list-table > table > tbody.reactable-data > tr";
var list = document.querySelectorAll(selector)
list.forEach(v=>{
    var lock_list = v.getElementsByClassName("fa-lock")
    if (lock_list.length > 0) v.parentNode.removeChild(v)
});
console.log(list.length)
```

str去空格
```
var str = "h tt p:/ /p an.b ai du.c om/s/1 ntI Cni x";
str = str.replace(/\s+/g, "")
```

eval函数

eval() 函数可计算某个字符串，并执行其中的的 JavaScript 代码。

该方法只接受原始字符串作为参数，如果 string 参数不是原始字符串，那么该方法将不作任何改变地返回。因此请不要为 eval() 函数传递 String 对象来作为参数。

如果试图覆盖 eval 属性或把 eval() 方法赋予另一个属性，并通过该属性调用它，则 ECMAScript 实现允许抛出一个 EvalError 异常。

> http://www.w3school.com.cn/jsref/jsref_eval.asp


js 的变量可以跨js文件引用。


js为元素设置点击事件
```
<html lang="zh-CN">
<head>
 <meta charset="UTF-8">
<script type="text/javascript">
function get_img_index() {
document.write("<p id=\"content\">")
document.write("</p>")
var page_index = document.getElementById("content");
console.log(page_index)
return page_index;
}
</script>
</head>
<body>
<p onclick=get_img_index()>TTTT</p>
</body>
</html>

```


eval(function(p,a,c,k,e,d){...} 

这个是js中常见的加解密，要想得到结果可以直接在http://tool.chinaz.com/js.aspx进行解密，或者本地写好一个html页面，去掉只取eval的function部分通过Document.write来查看结果
```
<html lang="zh-CN">
<head>
 <meta charset="UTF-8">
<script type="text/javascript">
function get_img_index() {
document.write("<p id=\"content\">")
document.write(function(p,a,c,k,e,d){....})
document.write("</p>")
var page_index = document.getElementById("content");
console.log(page_index)
return page_index;
}
</script>
</head>
<body>
<p onclick=get_img_index()>TTTT</p>
</body>
</html>

```

1. F12和网页调试工具的区别  
查看网页源码」是服务器发回来的原始代码，而在开发者工具看到的是被 Javascript 动态修改过后的源码。  
源代码是由服务器渲染出来的。 2、F12是服务器渲染出来的代码再由浏览器（Js等，有可能是第三方插件：花瓣插件等）渲染出来的最终代码。
2. 

# 参考资料
1. []()