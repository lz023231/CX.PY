#有序字典
from collections import OrderedDict
#为了读取数据
from pyexcel_xls import get_data

def readXlsAndXlsxFile(path):
    dic = OrderedDict()
    #抓取数据
    xdate = get_data(path)

    for sheet in xdate:
        dic[sheet] = xdate[sheet]
    return dic


path = r"E:\CX.PY\自动化办公和鼠标键盘模拟\Excel办公自动化\1.xls"
dic = readXlsAndXlsxFile(path)
print(dic)
print(len(dic))

