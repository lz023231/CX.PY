import os
from multiprocessing import Pool
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




if __name__ =="__main__":
    # 读取path下的所有的文件
    fileslist = os.listdir(path)
    start = time.time()
    pp = Pool(4)
    for fileName in fileslist:
        pp.apply_async(copyFile,args=(os.path.join(path,fileName),os.path.join(topath,fileName)))
    pp.close()
    pp.join()
    end = time.time()
    print("总耗时：%.2f" % (end-start))