[TOC]

***使用约束布局创建响自适应的UI***   
  
约束布局可以允许开发者使用扁平的是视图层级结构(不适用布局嵌套)大型复杂的布局。和相对布局相似的是约束布局所有的视图都是通过周围视图和父布局之间的相对关系来确定位置的，但约束布局更加的灵活也更容易通过Android Studio的布局编辑器(Layout Editor)来创建约束布局。
  约束布局的所有功能都可以通过布局编辑器直接使用，因为布局编辑器和布局的相关的API为约束布局特别优化过。你完全可以通过布局编辑器拖拽控件来创建一个约束布局而不需要去编辑XML文件。
  约束布局所在的API Library兼容Android2.3(API 9)及以上，本文指导如何在Android Studio2.3及以上上面创建约束布局。如果你需要了解更多关于布局编辑器(Layout Editor)的事情，请参考Android Studio 的引导 **Build a UI With Layout Editor** 
  想知道那些布局约束布局可以创建，可以查看Github上面的约束布局的例子。
# 约束布局概览  
想确定视图在约束布局中的位置，你至少要为视图添加一个水平方向的约束一个垂直方向的约束。每一个约束代表与另外一个视图，父布局或者不可见的向导线(guidleLine)之间的联系或者对齐关系。每一张约束通过垂直轴或者水平轴定义了视图的位置。所以每个视图在每个方向上至少定义一个约束，通常在一个方向上需要多个约束。
当你拖拽一个视图进布局编辑器，如果没有约束视图将停留在你释放的位置上，但这只是为了你编辑方便，如果没有任何约束当部署到设备上时该视图将会显示屏幕的左上角坐标为(0,0)的位置上。
尽管缺失约束不会引起编译的错误，但布局编辑器将缺失约束当作错误显示在toolbar中，

# Add ConstraintLayout to your project

## Convert a layout

## Create a new layout
# Add a constraint
## Parent position
## Order position
## Alignment
## Baseline alignment
## Constrain to a guideline
# Adjust the constraint bias
# Adjust the view size 
# Set size as a ratio
# Adjust the view margins

# Control linear groups with a chain
# Automatically create constraints

优点：
1. 直接拖拽控件，改变以前xml布局文件基本靠写xml文件的模式
2. 解决布局嵌套导致的性能问题。
使用约束布局的要求限制：
1. 兼容性：最低Android2.3(API 9)

# 名词
约束拉手(constraint handle):
约束(constraint):
( Each constraint represents a connection or alignment to another view, the parent layout, or an invisible guideline)
基线(baseline)
垂直平面(vertical plane)
锚点(anchor point)：视图的边界，布局的边界，指导线。(the edge of another view, the edge of the layout, or a guideline）
约束：

创建约束的准则：
1. 每一个视图至少需要一个水平方向和一个垂直方向的约束。
2. 你只能在相同的平面上创建约束，比如说垂直平面(视图的左右边界)只能和视图的左右边界相约束，不能和水平平面即上下方向约束。基线只能和基线相约束。
3. 每一个约束拉手最多只能创建一个约束，而一个锚点可以创建多个约束(来之不同视图)

# 通过约束布局建立和交互界面
约束布局可以帮你创建一个复杂的但存在布局嵌套的布局，

# 原文地址
[Google约束布局使用指南](https://developer.android.google.cn/training/constraint-layout/index.html)
[使用ConstraintLayout(约束布局)构建响应式UI](https://www.pocketdigi.com/20170105/1525.html)

[CoordinatorLayout的官方资料](https://developer.android.google.cn/reference/android/support/design/widget/CoordinatorLayout.html)


