import tkinter
win = tkinter.Tk()
win.title("雷哥")
#win.geometry("400x400+200+20")


#EXTENDED可以使listbox支持shift和control
lb = tkinter.Listbox(win,selectmode = tkinter.EXTENDED)
lb.pack()
for item in ["good","nice", "cool" , "vn","ez""good1","nice1", "cool1" , "vn1","ez1","good2","nice2", "cool2" , "vn2","ez2"]:
    #按顺序添加
    lb.insert(tkinter.END,item)
#滚动条
sc = tkinter.Scrollbar(win)
sc.pack(side=tkinter.RIGHT,fill=tkinter.Y)
lb.configure(yscrollcommand=sc.set)
lb.pack(side=tkinter.LEFT,fill=tkinter.BOTH)
#额外给属性赋值
sc['command']=lb.yview


win.mainloop()














