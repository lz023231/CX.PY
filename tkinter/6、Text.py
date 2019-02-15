import tkinter
win = tkinter.Tk()
win.title("雷哥")
win.geometry("400x400+200+20")

'''
文本控件，用于显示多行文本
'''
#height表示显示的行数
text = tkinter.Text(win,width=30, height=4)
text.pack()
str = '''THE PRESIDENT: Hello, everybody! Thank you. Thank you. Thank you, everybody. All right, everybody go ahead and have a seat. How is everybody doing today? (Applause.) How about Tim Spicer? (Applause.) I am here with students at Wakefield High School in Arlington, Virginia. And we've got students tuning in from all across America, from kindergarten through 12th grade. And I am just so glad that all could join us today. And I want to thank Wakefield for being such an outstanding host. Give yourselves a big round of applause. (Applause.) '''
text.insert(tkinter.INSERT,str)

win.mainloop()




