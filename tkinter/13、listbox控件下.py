import tkinter
win = tkinter.Tk()
win.title("雷哥")
win.geometry("400x400+200+20")

lb = tkinter.Listbox(win,selectmode = tkinter.MULTIPLE)
lb.pack()
for item in ["good","nice", "cool" , "ok", "vn","ez"]:
    lb.insert(tkinter.END,item)



win.mainloop()














