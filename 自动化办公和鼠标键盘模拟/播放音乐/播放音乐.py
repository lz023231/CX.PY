
import time
import pygame


#音乐路径
filePath = r"E:\CX.PY\自动化办公和鼠标键盘模拟\播放音乐\res\0.mp3"

#初始化
pygame.mixer.init()

#加载音乐
track = pygame.mixer.music.load(filePath)


#播放
pygame.mixer.music.play()
#暂停
time.sleep(66)


#停止
pygame.mixer.music.stop()








