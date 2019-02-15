import threading


def run():
    print("leige is a good man!")


#延时执行线程
t = threading.Timer(5,run)
t.start()
t.join()
print("主线程结束")





