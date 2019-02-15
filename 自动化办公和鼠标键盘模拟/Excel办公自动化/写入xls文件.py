#有序字典
from collections import OrderedDict
#为了写入数据
from pyexcel_xls import save_data

def makeExcelFile(path,date):
    dic = OrderedDict()
    for sheetName,sheetValue in date.items():
        d = {}
        d[sheetName] = sheetValue
        dic.update(d)
    save_data(path,dic)

path = r"E:\CX.PY\自动化办公和鼠标键盘模拟\Excel办公自动化\2.xls"
makeExcelFile(path,{"表1":[[1,2,3],[4,5,6],[7,8,9]],
                    "表2":[[11,22,33],[44,55,66],[77,88,99]]})