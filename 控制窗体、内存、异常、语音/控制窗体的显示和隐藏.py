import win32con
import win32gui
import time

#找出窗体的编号
QQWin = win32gui.FindWindows("类，名字")

#隐藏窗体
win32gui.ShowWindows(QQWin,win32con.SW_HIDE)

#显示窗体
win32gui.ShowWindows(QQWin,win32con.SW_SHOW)













