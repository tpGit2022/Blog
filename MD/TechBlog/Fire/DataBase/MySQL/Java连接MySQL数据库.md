先去MySQL官方下载连接驱动mysql-connector-java
https://dev.mysql.com/downloads/connector/j/

CREATE TABLE `hellotest`.`table2` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `table2col` VARCHAR(120) NULL,
  PRIMARY KEY (`id`));


```
public void connDataBase(List<SSPInfoBean> list){
        Connection con;
        String driver="com.mysql.jdbc.Driver";
        String url="jdbc:mysql://localhost:3306/xxx";
        String user="root";
        String passwd="xxxx";
        try {
            Class.forName(driver);
            con= DriverManager.getConnection(url,user,passwd);
            if(!con.isClosed())
                System.out.println("success connect database");            
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
```