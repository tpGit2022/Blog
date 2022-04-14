# Java
## 与或操作| || & &&的区别
|不管左右的值如何 两者都会执行判断 ||当左侧已是true值不再执行右侧的判断
即若str为null,str==null|str.equals("A")和str==null||str.equals("A"),前者会导致空指针异常，后者不会。  
&不管左右的值如何 两者都会执行判断 &&当左侧已是false值不再执行右侧的判断
即若str为null,str!=null&str.equals("A")和str!=null&&str.equals("A"),前者会导致空指针异常，后者不会
