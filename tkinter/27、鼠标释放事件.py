import tkinter
win = tkinter.Tk()
win.title("雷哥")
win.geometry("400x400+200+20")





#<ButtonRelease-1>释放鼠标左键
#<ButtonRelease-2>释放鼠标中键
#<ButtonRelease-3>释放鼠标右键
lable = tkinter.Label(win,text="leige is a good man!",bg="red")
lable.pack()
def func(event):
    print(event.x, event.y)
lable.bind("<ButtonRelease-1>", func)



win.mainloop()














