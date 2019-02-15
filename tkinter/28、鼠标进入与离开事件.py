import tkinter
win = tkinter.Tk()
win.title("雷哥")
win.geometry("400x400+200+20")

#<Enter>  鼠标光标进入控件时触发
#<Leave>  鼠标光标离开控件时触发
lable = tkinter.Label(win,text="leige is a good man!",bg="red")
lable.pack()
def func(event):
    print(event.x, event.y)
lable.bind("<Enter>", func)



win.mainloop()














