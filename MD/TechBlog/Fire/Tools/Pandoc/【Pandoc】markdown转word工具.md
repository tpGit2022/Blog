项目地址：https://github.com/jgm/pandoc/releases/tag/1.14.0.1

用法

`pandoc -f markdown -t docx ./test.md -o test.docx`

如果是github风格语法

`pandoc -f markdown_github -t docx ./test.md -o test.docx`


当然网上还有人说为了提高文档格式的还原度，先转换为 html 在转为 docx 可能更好：
`pandoc -f markdown -t html ./test.md | pandoc -f html -t docx -o test.docx`

稍微用批处理封装下保存下面代码为mdtodoc.bat
```
@echo off
rem 用于一键Markdown文档为docx文档，用法样例
rem 终端键入:mdtodoc 你的待转化markdown文档 输出文档名
echo "一键转化MarkDown文档为Docx文档"
rem 保存原来路径
set InitPath=%CD%
rem echo %1,%2
pandoc -f markdown_github -t html %1 | pandoc -f html -t docx -o %2.docx
echo 转换完成
rem 开启资源管理器窗口
start .
rem 还原原来的路径
rem echo %InitPath%
cd /d %InitPath%
exit
```
用法
> mdtodoc test.md test