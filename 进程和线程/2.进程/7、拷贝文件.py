import os
import time
from multiprocessing import Process
#实现文件的拷贝
def copyFile(rpath,wpath):
    fr = open(rpath,"rb")
    fw = open(wpath,"wb")
    context = fr.read()
    fw.write(context)

    fr.close()
    fw.close()

path = r"E:\CX.PY\进程和线程\2.进程\file"
topath = r"E:\CX.PY\进程和线程\2.进程\tofile"

#读取path下的所有的文件
fileslist = os.listdir(path)

#启动for循环处理每一个文件
start = time.time()
for fileName in fileslist:
    copyFile(os.path.join(path,fileName),os.path.join(topath,fileName))

end = time.time()
print("总耗时：%.2f" % (end-start))
