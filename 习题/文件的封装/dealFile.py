import csv
from collections import OrderedDict

import win32com
import win32com.client
import sys
import importlib
importlib.reload(sys)

from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
class DealFile(object):
    #读取CSV文件
    def readCsv(self,path):
        infoList = []
        with open(path, "r") as f:
            allFileInfo = csv.reader(f)
            print(allFileInfo)
            for row in allFileInfo:
                infoList.append(row)
        return infoList

    #写CSV
    # [[1,2,3],[1,2,3,],[4,5,6]]
    def writeCsv(self,path, date):
        with open(path, "w") as f:
            writer = csv.writer(f)
            for rowDate in date:
                writer.writerow(rowDate)

    def readPDF(self,path,callback=None ,toPath=""):
        f = open(path, "rb")
        parser = PDFParser(f)
        pdfFile = PDFDocument()
        parser.set_document(pdfFile)
        pdfFile.set_parser(parser)
        pdfFile.initialize()
        if not pdfFile.is_extractable:
            raise PDFTextExtractionNotAllowed
        else:
            manager = PDFResourceManager()
            laparams = LAParams()
            device = PDFPageAggregator(manager, laparams=laparams)
            interpreter = PDFPageInterpreter(manager, device)
            for page in pdfFile.get_pages():
                interpreter.process_page(page)
                layout = device.get_result()
                for x in layout:
                    if (isinstance(x, LTTextBoxHorizontal)):
                        if toPath == "":
                            #处理每行数据
                            str = x.get_text()
                            if callback != None:
                                callback(str)
                            else:
                                print(str)
                        else:
                            #写文件
                            print("将PDF数据写入文件")

    def readWordFile(path):
        mw = win32com.client.Dispatch("word.Application")
        doc = mw.Documents.Open(path)
        for paragraph in doc.Paragraphs:
            line = paragraph.Range.Text
            print(line)
        doc.Close()
        mw.Quit()

    def makePPT(path):
        ppt = win32com.client.Dispatch(PowerPoint.Application)
        ppt.Visible = True
        pptFile = ppt.Presentations.Add()
        page1 = pptFile.Slides.Add(1, 1)
        t1 = page1.Shapes[0].TextFrame.TextRange
        t1.Text = "leige"
        t2 = page1.Shapes[1].TextFrame.TextRange
        t2.Text = "leige is a good man!"
        page2 = pptFile.Slides.Add(1, 1)
        t3 = page2.Shapes[0].TextFrame.TextRange
        t3.Text = "leige"
        t4 = page2.Shapes[1].TextFrame.TextRange
        t4.Text = "leige is a good man!"
        pptFile.SaveAs(path)
        pptFile.Close()
        ppt.Quit()

    def readXlsAndXlsxFile(path):
        dic = OrderedDict()
        # 抓取数据
        xdate = get_data(path)

        for sheet in xdate:
            dic[sheet] = xdate[sheet]
        return dic