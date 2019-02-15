import threading

num = 0
#创建一个全局的ThreadLoacl对象
#每个线程由独立的存储空间
#每个线程对ThreadLoacl对象都可以读写，但是互不影响
local = threading.local()
def run(x,n):
    x = x + n
    x = x - n
def func(n):
    #每个线程都有一个local.x,就是线程的局部变量
    local.x = num
    for i in range(10000):
        run(local.x,n)
    print("%s-%d"%(threading.current_thread().name,local.x))


if __name__ =="__main__":
    t1 = threading.Thread(target=func,args=(6,))
    t2 = threading.Thread(target=func,args=(9,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("num =" ,num)

#作用：为每个线程绑定一个数据库，HTTP，请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便的访问这些资源

















