https://www.mysql.com/products/connector/

Java操作MySQL数据库需要额外的jar包支持,去往MySQL官方下载Java连接需要的jar包`https://www.mysql.com/products/connector/`,先了解下JDBC，JDBC是Java用于和数据库(MySQL,SQLSERVER,SQLite...)打交道的，JDBC全称Java Database Connectivity,用于Java语言规范访问数据库的。
Java语言操作数据库的基本步骤
1. 加载相关的数据库驱动
2. 执行相关的sql语句。

下载好相关的驱动jar包后通过以下代码来加载
```
String driverName="com.mysql.jdbc.Driver";
Class.forName(driverName);//动态加载MySQL的驱动
String url="jdbc:mysql://"+host+dbName;//"jdbc:mysql://localhost:3306/samp_db"
Connection conn= DriverManager.getConnection(url,username,passwd);
if(!conn.isClosed()){
    System.out.println(host+"数据库连接成功!");
}
```


执行查询语句

```
 public void queryAll(Connection conn,String Table) throws SQLException {
        String sql="select * from  "+Table;
        PreparedStatement ps;
        ps=conn.prepareStatement(sql);
        ResultSet rs=ps.executeQuery();
        int colCount=rs.getMetaData().getColumnCount();
        while (rs.next()){
            for(int i=1;i<=colCount;i++){//注意下标的开始位置1 开始不是0
                System.out.print(rs.getString(i)+"\t");
            }
            System.out.println("\n");
        }
    }
```

简单封装一下：
数据库连接，当然这种方式不大靠谱因为没有关闭数据库连接，平常用用就行。
```
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class MySQLConnectManager {
    private  volatile static Connection conn=null;
    private static MySQLConnectManager mInstance=new MySQLConnectManager();
    private MySQLConnectManager(){

    }
    public static MySQLConnectManager getInstance(){
        return mInstance;
    }
    /**
     * 获取MySQL的连接,需要手动关闭数据库连接
     * @param dbName  数据库名称
     * @param username  数据库的用户名
     * @param passwd  数据库的密码
     * @return
     * @throws ClassNotFoundException
     * @throws SQLException
     */
    public Connection getConnect(String host,String dbName,String username,String passwd) throws ClassNotFoundException, SQLException {
        if(conn==null){
            synchronized (MySQLConnectManager.class){
                if(conn==null){
                    String driverName="com.mysql.jdbc.Driver";
                    Class.forName(driverName);//动态加载MySQL的驱动
                    String url="jdbc:mysql://"+host+dbName;//"jdbc:mysql://localhost:3306/samp_db"
                    conn= DriverManager.getConnection(url,username,passwd);
                    if(!conn.isClosed()){
                        System.out.println(host+"数据库连接成功!");
                    }
                }
            }
        }
        return conn;
    }

    /**
     * 用于快速连接本地的MySQL数据库
     * @param dbName 数据库名称
     * @param username 数据库的用户名
     * @param passwd  数据库密码
     * @return
     * @throws ClassNotFoundException
     * @throws SQLException
     */
    public Connection getConnect(String dbName,String username,String passwd)throws ClassNotFoundException, SQLException {
        return this.getConnect("localhost:3306/",dbName,username,passwd);
    }
}
```

数据的操作类(增删读写)
```
import mysql.Bean.StudentBasicInfo;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

/**
 * MySQL 数据库操作类
 */
public class MySQLBasicOperate {
    /**
     * 创建表
     * @param conn
     * @param tableName
     */
    public void createTable(Connection conn,String tableName) throws SQLException {
        String sql="CREATE TABLE `student_basic` (\n" +
                "  `id` varchar(30) NOT NULL,\n" +
                "  `Name` varchar(50) DEFAULT NULL,\n" +
                "  `Age` int(11) DEFAULT NULL\n" +
                ") ENGINE=InnoDB DEFAULT CHARSET=utf8";
        PreparedStatement ps=conn.prepareStatement(sql);
        ps.execute(sql);
    }

    /**
     * 插入新数据
     * @param conn
     * @param bean
     * @throws SQLException
     */
    public void insertRecord(Connection conn,StudentBasicInfo bean) throws SQLException {
        String sql="INSERT INTO student_basic(id,Name,Age) VALUES (?,?,?);";
        PreparedStatement ps=conn.prepareStatement(sql);
        ps.setString(1,bean.getId());
        ps.setString(2,bean.getName());
        ps.setInt(3,bean.getAge());
        int i=ps.executeUpdate();
        System.out.println(i+"行受影响");
        ps.close();
    }

    /**
     * 删除数据
     * @param conn
     * @param Id
     * @throws SQLException
     */
    public void deleteRecord(Connection conn,String Id) throws SQLException {
        String sql="DELETE FROM student_basic WHERE Id='"+Id+"'";
        PreparedStatement ps=conn.prepareStatement(sql);
        int i=ps.executeUpdate();
        System.out.println("已删除"+i+"行");
        ps.close();
    }
    /**
     * 查询某张表中的所有数据
     * @param conn
     * @param tableName
     * @throws SQLException
     */
    public void queryAll(Connection conn,String tableName) throws SQLException {
        String sql="select * from  "+tableName;
        PreparedStatement ps;
        ps=conn.prepareStatement(sql);
        ResultSet rs=ps.executeQuery();
        int colCount=rs.getMetaData().getColumnCount();
        while (rs.next()){
            for(int i=1;i<=colCount;i++){//注意下标的开始位置1 开始不是0
                System.out.print(rs.getString(i)+"\t");
            }
            System.out.println("\n");
        }
        rs.close();
        ps.close();
    }

    /**
     * 更新数据
     * @param conn
     */
    public void updateRecord(Connection conn,StudentBasicInfo bean) throws SQLException {
        String sql="UPDATE student_basic SET NAME ='"+bean.getName()+"'"+"WHERE Id='"+bean.getId()+"'";
        PreparedStatement ps=conn.prepareStatement(sql);
        int i=ps.executeUpdate();
        System.out.println("已更新"+i+"行");
        ps.close();
    }
}

```