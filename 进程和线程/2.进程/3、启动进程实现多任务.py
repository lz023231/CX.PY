'''
multiprossing 库
跨平台版本的多进程模块，提供了Process类来代表一个进程对象
'''
from multiprocessing import Process
import os
from time import sleep

def run(str):
    while True:
        #os.getpid()获取当前进程ID号
        #os.getppid()获取当前进程的父进程ID号
        print("leige is a %s man!--%s--%s" % (str,os.getpid(),os.getppid()))
        sleep(1.2)

if __name__ =="__main__":
    print("主进程启动-%s" % (os.getpid()))
    #创建子进程
    #target说明进程执行的任务
    p = Process(target=run,args=("nice",))
    #启动进程
    p.start()


    while True:
        print("leige is a good man!")
        sleep(1)







