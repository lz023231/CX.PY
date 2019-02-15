import tkinter
win = tkinter.Tk()
win.title("雷哥")
win.geometry("400x400+200+20")
'''
Label:标签控件，可以显示文本
'''

#qwin:父窗体
#text   显示的文本内容
#bg   背景色
#fg   字体颜色
#wraplength  指定文本中多款进行换行
#justify   设置换行后的对其方式
#anchor  位置  n北  e东  s南   w西
label = tkinter.Label(win, text = "sunck",
                            bg = "blue",
                            fg = "red",
                            font = ("黑体", 20),
                            width = 10,
                            height = 4,
                            wraplength = 90,
                            justify = "left",
                            anchor = "n")
#显示出来
label.pack()







win.mainloop()




