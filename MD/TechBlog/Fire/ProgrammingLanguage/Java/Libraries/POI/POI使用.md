[TOC]


# 介绍

Apache POI 用于操作doc，ppt，xls等数据，该库只能用于Java平台不能用于Android，Android端考虑使用更轻便的jxl库 


jxl 读取 xlsx 文件时可能会报如下错误：

`jxl读取excel文件异常：Unable to recognize OLE stream` 因为是 jxl不支持 xlsx 文件读写

Gradle 引入依赖

```groovy
// https://mvnrepository.com/artifact/org.apache.poi/poi
    implementation 'org.apache.poi:poi:5.2.2'
    implementation 'org.apache.poi:poi-ooxml:5.2.2'   // add this for xlsx
```

`HSSFWorkbook` 用于操作xls

`XSSFWorkbook` 用于操作 xlsx


# POI的使用和常用API说明


读数据

```java
    public void parseXlsWithPOI() {
        String path = "xxxxx.xlsx";
        try {
            Workbook workbook = new XSSFWorkbook(path);
            int sheetCount = workbook.getNumberOfSheets();
            StringBuilder sb = new StringBuilder();
            for (int sheetIndex = 0; sheetIndex < sheetCount; sheetIndex++) {
                Sheet sheet = workbook.getSheetAt(sheetIndex);
                for (int r = 0; r < sheet.getLastRowNum(); r++) {
                    Row row = sheet.getRow(r);
                    if (row == null) continue;
                    int columns = row.getLastCellNum();
                    sb.delete(0, sb.length());
                    sb.append(String.format("第%d行", r));
                    for (int c = 0; c < columns; c++) {
                        if (null == row.getCell(c) || row.getCell(c).getCellType() == CellType.BLANK) continue;
//                        System.out.print(row.getCell(c).getCellType() + " ");
                        String tp = null;
                        if (row.getCell(c).getCellType() == CellType.NUMERIC) {
                            tp = String.valueOf(row.getCell(c).getNumericCellValue());
                        }

                        if (row.getCell(c).getCellType() == CellType.STRING) {
                            tp = row.getCell(c).getStringCellValue();
                        }

                        if (row.getCell(c).getCellType() == CellType.FORMULA) {
                            tp = row.getCell(c).getCellFormula();
                        }
                        sb.append(c).append("->").append(tp).append(" ");
                    }
                    System.out.println(sb);
                }
                break;
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
```

写数据

```java

```

设置行的宽高，颜色

```java
xssfRow.setHeight((short) (30 * 20));	// 设置行高 该方法传递进去的值会被除以20
xssfWorkbook.getSheetAt(0).setColumnWidth(0,25 * 256); // 设置第1列的宽度 传递进去的值会被除以256
xssfWorkbook.getSheetAt(0).setColumnWidth(3,30 * 256); // 设置第4列的宽度 传递进去的值会被除以256
```

POI 设置颜色，布局之类需要借助 `CellStyle` 具体的之类

```java
                    XSSFCellStyle xssfCellStyle = xssfWorkbook.createCellStyle();
                    xssfCellStyle.setFillForegroundColor((short) 52); // #FF9900 设置为黄橘色
//                    xssfCellStyle.setFillBackgroundColor((short) 3);
                    xssfCellStyle.setFillPattern(FillPatternType.SOLID_FOREGROUND); //设置为填充模式
                    xssfCellStyle.setVerticalAlignment(VerticalAlignment.CENTER);  //设置为垂直居中
                    xssfRow.setRowStyle(xssfCellStyle);
```


设置单元格宽高，颜色

```java
                    XSSFCellStyle xssfCellStyle = xssfWorkbook.createCellStyle();
                    xssfCellStyle.setFillForegroundColor((short) 52); // #FF9900 设置为黄橘色
//                    xssfCellStyle.setFillBackgroundColor((short) 3);
                    xssfCellStyle.setFillPattern(FillPatternType.SOLID_FOREGROUND); //设置为填充模式
                    xssfCellStyle.setVerticalAlignment(VerticalAlignment.CENTER);  //设置为垂直居中
                    xsscell.setCellStyle(xssfCellStyle);
```


设置字体颜色和大小

```java

```


# 参考资料

1. [POI XssfCellStyle背景颜色对照](https://blog.csdn.net/Han_Yi_To/article/details/119644992)
2. [POI Excel列宽设置](https://blog.csdn.net/lipinganq/article/details/78090553)
3. [POI Excel行高设置](https://blog.csdn.net/lipinganq/article/details/78081300)
4. [【Apache POI】设置单元格字体、颜色、边框、对齐方式、Excel读取导入、解析工具类](https://codeantenna.com/a/ev16En4iI1)
5. [Java使用POI读取和写入Excel指南](https://www.cnblogs.com/Dreamer-1/p/10469430.html)