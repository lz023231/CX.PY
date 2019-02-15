import os


def getALLDirRE(path):
    stack = []
    stack.append(path)


    #处理栈，栈为空时结束循环
    while len(stack) != 0:
        #从栈里取出数据
        dirPath = stack.pop()
        filesList = os.listdir(dirPath)
        #处理每一个文件，如果是普通文件则打印，如果是目录则将该目录的底地址压栈
        for fileName in filesList:
            fileAbsPath = os.path.join(dirPath,fileName)
            if os.path.isdir(fileAbsPath):
                print("目录：",fileName)
                stack.append(fileAbsPath)
            else:
                print("普通文件:", fileName)

getALLDirRE(r"C:\Users\Administrator\Desktop\dir")






















