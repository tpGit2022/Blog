

# 响应托盘的点击事件


```
LRESULT CMyTimerDlg::onShowTask(WPARAM wParam,LPARAM lParam) 
//wParam接收的是图标的ID，而lParam接收的是鼠标的行为 
{ 
	if(wParam!=IDR_MAINFRAME) 
		return 1; 
	switch(lParam) 
	{ 
	case WM_RBUTTONUP://右键起来时弹出快捷菜单，这里只有一个“关闭” 
		{ 
			
			LPPOINT lpoint=new tagPOINT; 
			::GetCursorPos(lpoint);//得到鼠标位置 
			CMenu menu; 
			menu.CreatePopupMenu();//声明一个弹出式菜单 
			//增加菜单项“关闭”，点击则发送消息WM_DESTROY给主窗口（已 
			//隐藏），将程序结束。 
			menu.AppendMenu(MF_STRING,WM_DESTROY,"关闭"); 
			//确定弹出式菜单的位置 
			menu.TrackPopupMenu(TPM_LEFTALIGN,lpoint->x,lpoint->y,this); 
			//资源回收 
			HMENU hmenu=menu.Detach(); 
			menu.DestroyMenu(); 
			delete lpoint; 
		} 
		break; 
	case WM_LBUTTONDBLCLK://双击左键的处理 
		{ 
			this->ShowWindow(SW_SHOW);//简单的显示主窗口完事儿
			this->SetFocus();
		} 
		break; 
	} 
	return 0; 
}
```


托盘

```
// 初始化托盘的数据
	m_NotifyData.cbSize = sizeof(NOTIFYICONDATA);
	m_NotifyData.hWnd = this->m_hWnd; //接收托盘消息的窗口句柄 this指的当前dialog
	m_NotifyData.uID = IDI_ICON_APP; //自定义的托盘图标
	m_NotifyData.uFlags = NIF_MESSAGE | NIF_ICON | NIF_TIP;
	CString tip = L"Mes工具";
	lstrcpyn(m_NotifyData.szTip, tip, sizeof(tip)); //图标的提示字符
	m_NotifyData.uCallbackMessage = WM_TRAY_MESSAGE_DISPLAY;
	m_NotifyData.hIcon = ::LoadIcon(AfxGetInstanceHandle(),
		MAKEINTRESOURCE(IDI_ICON_APP));
// 上述代码一般放在 OnInitDialog()  函数中

// 在需要的地方调用如下代码
Shell_NotifyIcon(NIM_ADD, &m_NotifyData); // 在托盘区域显示图标
Shell_NotifyIcon(NIM_DELETE, &m_NotifyData); //删除托盘区域的显示图标

// 托盘右键显示菜单
// 托盘鼠标右键显示菜单
			CMenu* pPopup = m_TrayMenu.GetSubMenu(0);
			CPoint point;
			GetCursorPos(&point);
			pPopup->TrackPopupMenu(TPM_LEFTALIGN | TPM_RIGHTBUTTON | TPM_VERTICAL,
				point.x, point.y, AfxGetApp()->m_pMainWnd, TPM_LEFTALIGN);
```


窗口消息

```
ShowWindow(SW_HIDE); //最小化且任务栏不显示图标
SendMessage(WM_CLOSE, 0, 0); // 发送关闭窗口消息 关闭窗口

SendMessage(WM_SYSCOMMAND, SC_RESTORE, 0);//发送restore 用于托盘点击还原主界面
```

