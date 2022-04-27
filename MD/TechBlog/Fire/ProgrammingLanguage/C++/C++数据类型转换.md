[TOC]


# string-->LPCWSTR

```
	size_t size = m_cookiepath.size();
	wchar_t *buff = new wchar_t[size + 1];
	MultiByteToWideChar(CP_ACP, 0, m_cookiepath.c_str(), size, buff, size * sizeof(wchar_t));
	buff[size] = 0;
	.....
	// do you  work
	.....
	delete buff
```


# 参考资料

1. [【MFC】CString 与 string 间的转换](https://blog.csdn.net/Gordon_Wei/article/details/90443677)