from dealFile import DealFile

d = DealFile()

topath = r""

for i in range(2,5):
    path = r"E:\CX.PY\自动化办公和鼠标键盘模拟\读CSV文件\001" + str(i) + ".csv"
    listInfo = d.readCsv(path)
    d.writeCsv(topath,listInfo)

allInfo = d.readCsv(topath)