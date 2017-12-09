# -*- coding: utf-8 -*-

# pywin32 应用演示
# 目标：实现将列表中的单词自动翻译出来
# 项目进度：未完成！
#   20171208 实现了向文本框发送单词。问题暂时无法取回翻译结果


import time
import win32gui
import win32api 
import win32con 


# 从网络复制的模块：查找窗口句柄
def find_idxSubHandle(pHandle, winClass, index=0):
        """
        已知子窗口的窗体类名
        寻找第index号个同类型的兄弟窗口
        """
        assert type(index) == int and index >= 0
        handle = win32gui.FindWindowEx(pHandle, 0, winClass, None)
        while index > 0:
            handle = win32gui.FindWindowEx(pHandle, handle, winClass, None)
            index -= 1
        return handle

def find_subHandle(pHandle, winClassList):
        """
        递归寻找子窗口的句柄
        pHandle是祖父窗口的句柄
        winClassList是各个子窗口的class列表，父辈的list-index小于子辈
        """
        assert type(winClassList) == list
        if len(winClassList) == 1:
            return find_idxSubHandle(pHandle, winClassList[0][0], winClassList[0][1])
        else:
            pHandle = find_idxSubHandle(pHandle, winClassList[0][0], winClassList[0][1])
            return find_subHandle(pHandle, winClassList[1:])


words = ['girl','boy','man','study']

yd_win_title = u"网易有道词典"
yd_win_hd = win32gui.FindWindow('YodaoMainWndClass',yd_win_title)
print('{} - {:x}'.format(yd_win_hd,yd_win_hd))
if int(yd_win_hd) <= 0 :
    print(yd_win_title,'未启动')
    exit(0)
    

yd_win2_hd=win32gui.FindWindowEx(yd_win_hd,None,None,None)
print('{} - {:x}'.format(yd_win2_hd,yd_win2_hd))

yd_win3_hd=find_subHandle(yd_win_hd,[('Edit',0)])
print('{} - {:x}'.format(yd_win3_hd,yd_win3_hd))

yd_win4_hd = find_subHandle(yd_win_hd,[('YodaoMainWndClass',0),
    ('CefBrowserWindow',0),
    ('Chrome_WidgetWin_0',0),
    ('Chrome_RenderWidgetHostHWND',0)])
print('{} - {:x}'.format(yd_win4_hd,yd_win4_hd))

#获取窗口焦点
win32gui.SetForegroundWindow(yd_win_hd)
win32gui.SetForegroundWindow(yd_win3_hd)


for word in words:
    # WM_SETTEXT
    win32api.SendMessage(yd_win3_hd,win32con.WM_SETTEXT,None,word)
    win32api.keybd_event(13,0,0,0)     # 回车键
    win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
    #win32gui.SetForegroundWindow(yd_win4_hd)
    time.sleep(2.5)