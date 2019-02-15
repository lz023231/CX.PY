import win32con
import win32api
import time

#设置鼠标的位置
win32api.SetCursorPos([20,40])
time.sleep(0.1)
#设置鼠标左键按下
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0)
#设置鼠标左键抬起
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0)




