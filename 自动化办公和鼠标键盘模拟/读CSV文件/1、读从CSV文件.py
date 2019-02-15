import csv
def readCsv(path):
    infoList = []
    with open(path, "r") as f:
        allFileInfo = csv.reader(f)
        print(allFileInfo)
        for row in allFileInfo:
            infoList.append(row)
    return infoList



path = r"E:\CX.PY\自动化办公和鼠标键盘模拟\读CSV文件\001.csv"
info = readCsv(path) #读出来的文件
