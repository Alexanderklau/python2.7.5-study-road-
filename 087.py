import Tkinter
top = Tkinter.Tk()#顶层窗口
hello = Tkinter.Label(top,text = 'hello world!')
hello.pack()
quit = Tkinter.Button(top,text='QUIT',command = top.quit,bg = 'red',fg = 'white')
quit.pack(fill=Tkinter.X,expand=1)
Tkinter.mainloop()