import tkinter
win = tkinter.Tk()
win.title("雷哥")
win.geometry("400x400+200+20")

#<B1-Motion>  左键移动
#<B2-Motion>  中键移动
#<B3-Motion>  右键移动
lable= tkinter.Label(win,text="leige is a good man")
lable.pack()

def func(event):
    print(event.x, event.y)
lable.bind("<B1-Motion>", func)

win.mainloop()














