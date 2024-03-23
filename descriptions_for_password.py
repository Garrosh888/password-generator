from tkinter import *
def click_cancel():
    window.destroy()

window = Tk()
window.resizable(0,0)
window.title("sftc")
cnv = Canvas(window,width=300,height=200)
cnv.pack()
cnv.create_text(70,10,anchor=NW,text = "введите описание",font=(None,15))
descriptions = Text(cnv,font=(None,10),width=30,height=5)
descriptions.place(x=40,y=50 )
save_btn = Button(cnv,text= "save",font=(None,15))
save_btn.place(x= 40,y= 150)
cancel_btn = Button(cnv,text= "cancel",font=(None,15),command=click_cancel)
cancel_btn.place(x= 180,y= 150)
window.mainloop()