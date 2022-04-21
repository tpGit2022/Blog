[TOC]


剪切板中的数据类型

```cplusplus
/*
 * Predefined Clipboard Formats
 */
#define CF_TEXT             1
#define CF_BITMAP           2
#define CF_METAFILEPICT     3
#define CF_SYLK             4
#define CF_DIF              5
#define CF_TIFF             6
#define CF_OEMTEXT          7
#define CF_DIB              8   QQ截图获取到的类型
#define CF_PALETTE          9
#define CF_PENDATA          10
#define CF_RIFF             11
#define CF_WAVE             12
#define CF_UNICODETEXT      13   文本内容
#define CF_ENHMETAFILE      14
#if(WINVER >= 0x0400)
#define CF_HDROP            15   文件和文件夹类型
#define CF_LOCALE           16
#endif /* WINVER >= 0x0400 */
#if(WINVER >= 0x0500)
#define CF_DIBV5            17   微软画板复制类型
#endif /* WINVER >= 0x0500 */

#if(WINVER >= 0x0500)
#define CF_MAX              18
#elif(WINVER >= 0x0400)
#define CF_MAX              17
#else
#define CF_MAX              15
#endif

#define CF_OWNERDISPLAY     0x0080
#define CF_DSPTEXT          0x0081
#define CF_DSPBITMAP        0x0082
#define CF_DSPMETAFILEPICT  0x0083
#define CF_DSPENHMETAFILE   0x008E
```



```cplusplus

if (OpenClipboard())//打开剪贴板  
 {  
  if (IsClipboardFormatAvailable(CF_TEXT))//判断格式是否是我们所需要  
  {  
   HANDLE hClip;  
   char* pBuf;  
   
//读取数据  
   hClip=GetClipboardData(CF_TEXT);  
   pBuf=(char*)GlobalLock(hClip);  
   GlobalUnlock(hClip);  
   SetDlgItemText(IDC_EDIT_RECV,pBuf);//讲数据显示在IDC_EDIT_RECV中  
   CloseClipboard();  
  }  
 }  
 

 

if (OpenClipboard())//打开剪贴板  
 {  
  CString str;  
  HANDLE hClip;  
  char* pBuf;  
  EmptyClipboard();//清空剪贴板  
  GetDlgItemText(IDC_EDIT_SEND,str);//获取IDC_EDIT_SEND中的数据  
   
//写入数据  
  hClip=GlobalAlloc(GMEM_MOVEABLE,str.GetLength()+1);  
  pBuf=(char*)GlobalLock(hClip);  
  strcpy(pBuf,str);  
  GlobalUnlock(hClip);//解锁  
  SetClipboardData(CF_TEXT,hClip);//设置格式  
   
//关闭剪贴板  
  CloseClipboard();  
 }  


```


# 参考资料