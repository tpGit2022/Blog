POI 框架用于Java语言解析Excel。官方地址:https://poi.apache.org/
官方介绍:
```
The Apache POI Project's mission is to create and maintain Java APIs for manipulating various file formats based upon the Office Open XML standards (OOXML) and Microsoft's OLE 2 Compound Document format (OLE2). In short, you can read and write MS Excel files using Java. In addition, you can read and write MS Word and MS PowerPoint files using Java. Apache POI is your Java Excel solution (for Excel 97-2008). We have a complete API for porting other OOXML and OLE2 formats and welcome others to participate.
```

简单译过来就是利用该框架可以读写微软的Excel文件。

在mvnrespository的地址为`http://mvnrepository.com/artifact/org.apache.poi/poi`
当前最新的3.17版的jar包下载地址:`http://central.maven.org/maven2/org/apache/poi/poi/3.17/poi-3.17.jar`.

基本使用
```
private static  void readSheet() throws IOException {
        List<StudentInfo> list=new ArrayList<>();
        POIFSFileSystem fs=new POIFSFileSystem(new FileInputStream("全校学生信息表-中小学.xls"));
        HSSFWorkbook wb=new HSSFWorkbook(fs);
        HSSFSheet sheet=wb.getSheetAt(0);
        StudentInfo studentInfo;
        for(int i=0;i<sheet.getLastRowNum();i++){
            HSSFRow row=sheet.getRow(i);
            studentInfo=new StudentInfo();
            studentInfo.setId(row.getCell(0).getStringCellValue());
            studentInfo.setName(row.getCell(1).getStringCellValue());
            studentInfo.setGender(row.getCell(2).getStringCellValue());
            studentInfo.setGrade(row.getCell(3).getStringCellValue());
            studentInfo.setClassRange(row.getCell(4).getStringCellValue());
            list.add(studentInfo);
        }
        //遍历list
        for(StudentInfo info:list){
            System.out.println(info.toString());
        }
    }
```