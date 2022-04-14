CSS(Cascading Style Sheets):层叠样式表.样式表对于网页而言更类似于皮肤的意味。通过CSS可以很方便的针对整个网页或者网页元素进行颜色，大小等等属性的调整修改，通过CSS选择器选择特定的元素对元素的属性进行赋值是CSS对网页元素的基础。
先稍微讲点Html中的概念，
Tag:被称之为标签，每个标签有name和多个属性attrs，例如`<a href="http://www.baidu.com"></a>`是一个Tag，Tag的`name`是`a`，而`href`是属性,`http://www.baidu.com`是`href`的属性值。

Tag有两个比较重要的属性`id`和`class`,一般来讲id是唯一的，而class可以有多个，不同class之前用空格分隔，例如:
```
<p class=cls1 cls2>
我是P标签。
</p>
```

DOM(Documents Object Model):文档对象模型。
从网络获取的html源码是个复杂的树结构其根节点的tag为`<html>`，通过对DOM的操作即可实现的网页的修改删除新增等操作，DOM一般具备以下的基本结构
```
<!DOCTYPE html>
<html lang="zh-cn">
    <head>
    ......
    </head>
    <body>
    ....
    </body>
</html>
```
一般在`head`节点中定义外部CSS和JS文件的路径的路径
在`body`节点中定义具体的网页内容。
稍微讲下HTML，CSS，JavaScript三者的关系，HTML负责内容的展示，CSS负责外观，JavaScript负责事件。
基于DOM结构衍生以下概念：
节点:每一个Tag都是一个节点
父节点:当前节点的前驱节点
子节点:当前节点的后继节点
子孙节点:当前节点的后继节点以及后继节点的后继节点依此类推直至DOM树结束。
兄弟节点:和当前节点处于同一层次的节点。
CSS有很多种类型的选择器，ID选择器和类(Class)选择器是比较常见的两种。
id选择器用`#`表示
类选择器用`.`表示

常用CSS选择器：
1. id选择器
2. 类选择器
3. 属性选择器
4. 派生选择器

# 参考链接
1. [CSS基础及CSS选择器语法](http://www.runoob.com/cssref/css-selectors.html)
2. [JavaScript](http://www.runoob.com/js/js-tutorial.html)
  

