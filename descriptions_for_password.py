from tkinter import *
from datetime import datetime
class Description():
    def  __init__(self,password):
        self.password = password
        self.create_window()
    def create_window(self):
        self.window = Tk()
        self.window.resizable(0, 0)
        self.window.title("sftc")
        self.cnv = Canvas(self.window, width=300, height=200)
        self.cnv.pack()
        self.cnv.create_text(70, 10, anchor=NW, text="введите описание", font=(None, 15))
        self.descriptions = Text(self.cnv, font=(None, 10), width=30, height=5)
        self.descriptions.place(x=40, y=50)
        self.save_btn = Button(self.cnv, text="save", font=(None, 15),command=self.click_save)
        self.save_btn.place(x=40, y=150)
        self.cancel_btn = Button(self.cnv, text="cancel", font=(None, 15), command=self.click_cancel)
        self.cancel_btn.place(x=180, y=150)
        #window.mainloop()
    def click_cancel(self):
        self.window.destroy()

    def click_save(self):
        with open("my passwords.txt","a") as password_file:#открытия файла в режиме для добавления текста

            now_day = datetime.now()
            info = f"{self.password} {now_day.day}.{now_day.month}.{now_day.year}" \
                   f" {now_day.hour}:{now_day.minute}:{now_day.second} - {self.descriptions.get('1.0','end')} \n"
            password_file.write(info)
        self.window.destroy()