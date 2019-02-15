import tkinter
win = tkinter.Tk()
win.title("雷哥")
win.geometry("400x400+200+20")
'''
竖直范围控件
'''

def update():
    print(v.get())



#绑定变量
v=tkinter.StringVar()
#increment  步长  默认为1
#values  最好不要与from_=0,to=100  increment=1同时使用
#values=(0,2,4,6,8)
#command  只要值改变就会执行对应的方法
sp=tkinter.Spinbox(win,from_=0,to=100,increment=1,textvariable=v,command=update)
sp.pack()
#赋值
v.set(20)
#取值
print(v.get())


win.mainloop()














