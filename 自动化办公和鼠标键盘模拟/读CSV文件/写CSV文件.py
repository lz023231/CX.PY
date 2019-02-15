import csv

def writeCsv(path,date):
    with open(path,"w") as f:
        writer = csv.writer(f)
        for rowDate in date:
            writer.writerow(rowDate)




path = r"E:\CX.PY\读CSV文件\002.csv"
writeCsv(path,[[1,2,3],[4,5,6],[7,8,9]])



