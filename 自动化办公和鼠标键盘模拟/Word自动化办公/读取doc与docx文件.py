import win32com
import win32com.client


def readWordFile(path):
    #调用系统Word功能，可以处理doc和docx两种文件
    mw = win32com.client.Dispatch("word.Application")
    #打开文件
    doc = mw.Documents.Open(path)
    for paragraph in doc.Paragraphs:
        line = paragraph.Range.Text
        print(line)
    #关闭文件
    doc.Close()
    #退出Word
    mw.Quit()


path = r"E:\CX.PY\自动化办公和鼠标键盘模拟\Word自动化办公\leige.docx"
readWordFile(path)

