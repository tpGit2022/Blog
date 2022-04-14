> Intellij Idea 2017.2.5
> Tomcat 8.5.24

下载后Tomcat解压后搭建后，配置好相关的环境变量。
Intellij Idea中创建新的项目。
New Project-Java Enterprise.
Application Server处选择New-Tomcat Server，如果你配置好了Tomcat相应的环境变量，弹窗的对话框中会帮你选择好Tomcat服务器。
![20171219114706.png](../../../Pictures\20171219\20171219114706.png)  
之后勾选Web Application，下方的Create web.xml会被默认勾选中，点击下一步选择好存储项目的路径。
![20171219114508.png](../../../Pictures\20171219\20171219114508.png)  


配置下输出目录和依赖目录，在WEB-INF创建子目录`classes`和`lib`，打开项目结构(Project Structure,快捷键Ctrl+shift+Alt+S)，Project Settings-Modules ，在Paths一栏修改`Output Path`为新建的classes目录，`Test output path`也修改为新建的classes目录
切换至Dependencies栏，点击右侧绿色加号`Jars or directories`选择新建的lib目录，在Choose Categories of Selected File中选择为Jar Directory