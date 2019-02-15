


#编码
path = r"C:\Users\Administrator\Desktop\cx.py\文件读写\file3.txt"
with open(path, "wb") as f1:
    str = "I am a good man!"
    f1.write(str.encode("utf-8"))


with open(path, "rb") as f2:
    data = f2.read()
    print(data)
    print(type(data))
    newData = data.decode("utf-8") #解码
    print(newData)
    print(type(newData))







