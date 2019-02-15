import win32com
import win32com.client


def readWordFileToOtherFile(path,toPath):
    mw = win32com.client.Dispatch("Word.Application")
    doc = mw.Documents.Open(path)

    #将Word的数据保存到另一个文件
    doc.SaveAs(toPath,2)  #2表示是一个TXT文件

    doc.Close()
    mw.Quit()


path = r"E:\CX.PY\自动化办公和鼠标键盘模拟\Word自动化办公\leige.docx"
toPath = r"E:\CX.PY\自动化办公和鼠标键盘模拟\Word自动化办公\a.txt"
readWordFileToOtherFile(path,toPath)

