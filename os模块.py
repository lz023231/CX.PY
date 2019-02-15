import os
'''
os:包含了普遍的操作系统的功能
'''
#获取操作系统类型
print(os.name)

#打印操作系统的详细信息，Windows不支持
#print(os.uname())

#获取操作系统的环境变量
#print(os.environ)
#获取指定环境变量
#print(os.environ.get("ALLUSERSPROFILE"))

#获取当前目录
#print(os.curdir)

#获取当前工作目录，即当前Python脚本所在的目录
#print(os.getcwd())
#返回指定目录下的所有的文件，以列表的形式返回
#print(os.listdir())

#在当前目录下创建新目录
#os.mkdir("fhiu")

#删除目录
#os.rmdir("fhiu")

#获取文件属性
#print(os.stat("fhiu"))

#重命名
#os.rename("fhiu", "dfhjwke")

#删除普通文件
#os.remove()

#运行shell命令
#os.system("notepad")
#os.system("write")
#os.system("mapaint")
#os.system("msconfig")
#os.system("shutdown -s -t 500")
#os.system("taskkill /f/im/notepad.exe")

#有些方法存在于os模块里，还有些存在于os.path里
#查看当前的绝对路径
#print(os.path.abspath("."))

#拼接路径
p1 = r"C:\Users\Administrator\Desktop\cx.py\文件读写"
p2 = "file1"  #开始不要有\
print(os.path.join(p1,p2))

#拆分路径
path2 = r"C:\Users\Administrator\Desktop\cx.py\文件读写"
print(os.path.split(path2))

#获取扩展名
print(os.path.splitext(path2))

#判断是否是目录
print(os.path.isdir(path2))


#判断文件是否存在
print(os.path.isfile(path2))

#判断目录是否存在
print(os.path.exists(path2))

#获得文件大小(字节)
print(os.path.getsize(path2))

#获得文件目录
print(os.path.dirname(path2))

#获得文件名
print(os.path.basename(path2))
