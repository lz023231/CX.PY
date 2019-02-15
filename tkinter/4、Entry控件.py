import tkinter
win = tkinter.Tk()
win.title("雷哥")
win.geometry("400x400+200+20")

'''
输入控件
用于显示简单的文本内容
'''
#绑定变量
e = tkinter.Variable()
# show  密文显示  show = "*"
entry = tkinter.Entry(win, textvariable=e)
entry.pack()

#在这之后e代表输入框这个对象
#设置值
e.set("leige is a good man!")
#取值
print(e.get())
print(entry.get())



win.mainloop()