import tkinter
win = tkinter.Tk()
win.title("雷哥")
win.geometry("400x400+200+20")

lable = tkinter.Label(win,text="leige is a good man!",bg="red")

#设置焦点
lable.focus_set()
lable.pack()
def func(event):
    print("event.char=", event.char)
    print("event.keycode=", event.keycode)
lable.bind("<Key>", func)


win.mainloop()














