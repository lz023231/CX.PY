


import tkinter
win = tkinter.Tk()
win.title("雷哥")
win.geometry("400x400+200+20")




def func(event):
    print("event.char=", event.char)
    print("event.keycode=", event.keycode)
win.bind("<Control-Alt-b>", func)


win.mainloop()


























