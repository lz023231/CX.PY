import time
import pygame
import win32api
import win32con
import win32gui
import threading

def go():
    pygame.mixer.init()
    while True:
        for i in range(5):
            filePath = r"E:\CX.PY\自动化办公和鼠标键盘模拟\整蛊小程序\res"+ "\\" + str(i) + ".mp3"
            track = pygame.mixer.music.load(filePath)
            pygame.mixer.music.play()
            time.sleep(10)
            pygame.mixer.music.stop()


def setWallPath(path):
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop", 0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(reg_key,"WallpaperStyle", 0,win32con.REG_SZ,"2")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,path, win32con.SPIF_SENDWININICHANGE)

th = threading.Thread(target=go, name = "LoopThread")
th.start()
while True:
    for i in range(10):
        filePath = r"E:\CX.PY\自动化办公和鼠标键盘模拟\整蛊小程序\res"+ "\\" + str(i) + ".jpg"
        setWallPath(filePath)
        time.sleep(1)



