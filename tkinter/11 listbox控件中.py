import tkinter
win = tkinter.Tk()
win.title("雷哥")
win.geometry("400x400+200+20")
#绑定变量
lbv = tkinter.StringVar()

#与BORWSE相似，但是不支持鼠标移动选中位置
lb = tkinter.Listbox(win,selectmode = tkinter.SINGLE,listvariable=lbv)
lb.pack()
for item in ["good","nice", "cool" , "ok", "vn","ez"]:
    #按顺序添加
    lb.insert(tkinter.END,item)



#打印当前列表中的选项
print(lbv.get())
#设置选项
#lbv.set(("1","2","3"))

#绑定事件
def myPrint(event):
    print(lb.get(lb.curselection()  ))
lb.bind("<Double-Button-1>",myPrint)





win.mainloop()














