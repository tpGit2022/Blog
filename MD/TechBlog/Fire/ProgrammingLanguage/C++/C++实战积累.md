C++中常见的文件类型：
`.cpp` : 源文件包含方法的定义
`.h` : 源文件主要是变量的定义和方法的声明
`.o` : Linux环境下源文件编译后的直接产物
`.exe` : 生成的可执行文件
`.dll` : 动态链接库
`.obj` : Windows环境下源文件编译后的直接产物

include 宏指令
`include <xxxx>` : 引用系统头文件
`include "xxxxx"`  : 引用用户自定义的头文件。



# 时间获取


C++获取时间存在精度问题，C++ 的API和 WindowsApi 需要区分一下 ，WindowsApi是不适用于Linux/Unix系统的


VC++ 获取系统时间、程序运行时间(精确到秒，毫秒)的五种方法
1.使用CTime类（获取系统当前时间，精确到秒）

CString str;
//获取系统时间
CTime tm;
tm=CTime::GetCurrentTime();//获取系统日期
str=tm.Format("现在时间是%Y年%m月%d日 %X");
MessageBox(str,NULL,MB_OK);
a，从CTimet中提取年月日时分秒 
复制代码
1 Time t = CTime::GetCurrentTime();
2 　int d=t.GetDay(); //获得几号
3 　int y=t.GetYear(); //获取年份
4 　int m=t.GetMonth(); //获取当前月份
5 　int h=t.GetHour(); //获取当前为几时
6 　int mm=t.GetMinute(); //获取分钟
7 　int s=t.GetSecond(); //获取秒
8 　int w=t.GetDayOfWeek(); //获取星期几，注意1为星期天，7为星期六
复制代码
b，计算两段时间的差值，可以使用CTimeSpan类，具体使用方法如下：
复制代码
1 CTime t1( 1999, 3, 19, 22, 15, 0 );
2 CTime t = CTime::GetCurrentTime();
3 CTimeSpan span=t-t1; //计算当前系统时间与时间t1的间隔
4 int iDay=span.GetDays(); //获取这段时间间隔共有多少天
5 int iHour=span.GetTotalHours(); //获取总共有多少小时
6 int iMin=span.GetTotalMinutes();//获取总共有多少分钟
7 int iSec=span.GetTotalSeconds();//获取总共有多少秒
复制代码
c，获得当前日期和时间，并可以转化为CString
 

1 CTime tm=CTime::GetCurrentTime(); 
2 CString str=tm.Format("%Y-%m-%d");//显示年月日
2.使用GetLocalTime：Windows API 函数，获取当地的当前系统日期和时间 （精确到毫秒）
　此函数会把获取的系统时间信息存储到SYSTEMTIME结构体里边
复制代码
typedef struct _SYSTEMTIME
{
WORD wYear;//年
WORD wMonth;//月
WORD wDayOfWeek;//星期：0为星期日，1为星期一，2为星期二……
WORD wDay;//日
WORD wHour;//时
WORD wMinute;//分
WORD wSecond;//秒
WORD wMilliseconds;//毫秒
}SYSTEMTIME,*PSYSTEMTIME;
复制代码
例：
复制代码
1 SYSTEMTIME st;
2 CString strDate,strTime;
3 GetLocalTime(&st);
4 strDate.Format("%4d-%2d-%2d",st.wYear,st.wMonth,st.wDay);
5 strTime.Format("%2d:%2d:%2d",st.wHour,st.wMinute,st.wSecond) ;
6 AfxMessageBox(strDate);
7 AfxMessageBox(strTime);
复制代码
3.使用GetTickCount：从操作系统启动到现在所经过（elapsed）的毫秒数，它的返回值是DWORD。（精确到毫秒）
复制代码
 1 //获取程序运行时间
 2 long t1=GetTickCount();//程序段开始前取得系统运行时间(ms)
 3 Sleep(500);
 4 long t2=GetTickCount();();//程序段结束后取得系统运行时间(ms)
 5 str.Format("time:%dms",t2-t1);//前后之差即 程序运行时间
 6 AfxMessageBox(str);
 7 //获取系统运行时间
 8 long t=GetTickCount();
 9 CString str,str1;
10 str1.Format("系统已运行 %d时",t/3600000);
11 str=str1;
12 t%=3600000;
13 str1.Format("%d分",t/60000);
14 str+=str1;
15 t%=60000;
16 str1.Format("%d秒",t/1000);
17 str+=str1;
18 AfxMessageBox(str);
复制代码
4.使用time_t time( time_t * timer ) ：   仅使用C标准库（精确到秒）
得到从标准计时点（一般是1970年1月1日午夜）到当前时间的秒数 
计算时间差：double difftime( time_t timer1, time_t timer0）
struct tm *localtime(const time_t *timer);  取得当地时间，localtime获取的结果由结构tm返回 
返回的字符串可以依下列的格式而定： 
%a 星期几的缩写。Eg:Tue 
%A 星期几的全名。 Eg: Tuesday 
%b 月份名称的缩写。 
%B 月份名称的全名。 
%c 本地端日期时间较佳表示字符串。 
%d 用数字表示本月的第几天 (范围为 00 至 31)。日期 
%H 用 24 小时制数字表示小时数 (范围为 00 至 23)。 
%I 用 12 小时制数字表示小时数 (范围为 01 至 12)。 
%j 以数字表示当年度的第几天 (范围为 001 至 366)。 
%m 月份的数字 (范围由 1 至 12)。 
%M 分钟。 
%p 以 ''AM'' 或 ''PM'' 表示本地端时间。 
%S 秒数。 
%U 数字表示为本年度的第几周，第一个星期由第一个周日开始。 
%W 数字表示为本年度的第几周，第一个星期由第一个周一开始。 
%w 用数字表示本周的第几天 ( 0 为周日)。 
%x 不含时间的日期表示法。 
%X 不含日期的时间表示法。 Eg: 15:26:30 
%y 二位数字表示年份 (范围由 00 至 99)。 
%Y 完整的年份数字表示，即四位数。 Eg:2008 
%Z(%z) 时区或名称缩写。Eg:中国标准时间 
%% % 字符。 

含：年，月，日，周几，小时，分，秒，毫秒。[喝小酒的网摘]http://blog.const.net.cn/a/16370.htm



# 参考资料

1. [VC++ 获取系统时间、程序运行时间(精确到秒，毫秒)的五种方法](https://www.cnblogs.com/lpxblog/p/5330693.html)
2. [mfc中CString如何转化为const char*类型？](https://www.zhihu.com/question/53686918)
3. [CString与LPCWSTR、LPWSTR等数据类型的转换](https://blog.csdn.net/zyw_anquan/article/details/8925565)