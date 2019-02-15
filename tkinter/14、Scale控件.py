import tkinter
win = tkinter.Tk()
win.title("雷哥")
win.geometry("400x400+200+20")
'''
供用户通过拖拽指示器改变变量的值，可以水平也可以竖直
tkinter.HORIZONTAL  水平
tkinter.VERTICAL   竖直（默认）
length  水平时表示宽度，竖直时表示高度
tickinterval  选择值将会为该值的倍数

'''
scale = tkinter.Scale(win,from_=0,to=100,orient=tkinter.HORIZONTAL,tickinterval=100,length=200)
scale.pack()
#设置值
scale.set(20)
#取值
def showNum():
    print(scale.get())
tkinter.Button(win,text="按钮",command=showNum).pack()


win.mainloop()














