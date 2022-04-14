http://mvnrepository.com/artifact/org.xerial/sqlite-jdbc

同样下载相关的jar。

加载SQLite的驱动
```
 public Connection getConnect(String path,String dbName) throws ClassNotFoundException, SQLException {
        if(conn==null){
            synchronized (SQLiteConnectManager.class){
                if(conn==null){
                    String driverName="org.sqlite.JDBC";
                    Class.forName(driverName);//动态加载MySQL的驱动
                    String url="jdbc:sqlite:"+path+dbName;//"jdbc:sqlite:test.db"
                    conn= DriverManager.getConnection(url);
                    if(!conn.isClosed()){
                        System.out.println(path+dbName+"数据库连接成功!");
                    }
                }
            }
        }
        return conn;
    }

```

