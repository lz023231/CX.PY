import os
import collections
def work(path):
    resPath = r"C:\Users\Administrator\Desktop\res"
    #打开文件
    with open(path,"r") as f:
        while True:
            #laphae11985@163.com----198587
            lineInfo = f.readline()
            if len(lineInfo) < 5:
                break
            #邮箱的字符串laphae11985@163.com
            mailStr =lineInfo.split("----")[0]
            #邮箱类型目录C:\Users\Administrator\Desktop\dir\res\163"
            fileType = mailStr.split("@")[1].split(".")[0]
            dirStr = os.path.join(resPath,fileType)
            if not os.path.exists(dirStr):
                #不存在，创建
                os.mkdir(dirStr)

            filePath = os.path.join(dirStr, fileType + ".txt")
            with open(filePath,"a") as fw:
                fw.write(mailStr +"\n")
            #创建文件

def getAllDirQU(path):
    queue = collections.deque()
    queue.append(path)
    while len(queue) != 0:
        dirPath = queue.popleft()
        filesList = os.listdir(dirPath)
        for fileName in filesList:
            fileAbsPath = os.path.join(dirPath,fileName)
            if os.path.isdir(fileAbsPath):
                queue.append(fileAbsPath)
            else:
                #处理普通文件
                work(fileAbsPath)


getAllDirQU(r"C:\Users\Administrator\Desktop\dir")



















