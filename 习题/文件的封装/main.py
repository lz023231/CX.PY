from dealFile import DealFile



d = DealFile()
path = r"E:\CX.PY\习题\文件的封装\001.pdf"

#因为dealFile里面有callback参数，所以梳理数据可以直接在main里面处理，如下
def func(str):
    print(str + "!")


d.readPDF(path,func)