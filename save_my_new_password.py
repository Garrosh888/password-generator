from tkinter import *
from datetime import datetime

class Description_from_me():
    def  __init__(self,save_password):
        self.create_window()
        self.save_password = save_password
    def create_window(self):
        self.window = Tk()
        self.window.resizable(0, 0)
        self.window.title("sftc")
        self.cnv = Canvas(self.window, width=300, height=300,bg="#afdec2")
        self.cnv.pack()
        self.cnv.create_text(70,10,anchor=NW, text="введите пароль", font=(None,15))
        self.password_entry = Entry(self.cnv,font=(None,10),width= 30)
        self.password_entry.place(x=40,y=50)
        self.cnv.create_text(70, 75, anchor=NW, text="введите описание", font=(None,15))
        self.descriptions = Text(self.cnv, font=(None, 10), width=30, height=5)
        self.descriptions.place(x=40, y=110)
        self.save_btn = Button(self.cnv, text="save", font=(None, 15),bg= "green",command=self.click_save)
        self.save_btn.place(x=40, y=225)
        self.cancel_btn = Button(self.cnv, text="cancel", font=(None, 15),bg="red", command=self.click_cancel)
        self.cancel_btn.place(x=180, y=225)
        #window.mainloop()
    def click_cancel(self):
        self.window.destroy()

    def click_save(self):
        if len(self.password_entry.get()) == 0:
            return
        with open("my passwords.txt","a") as password_file:#открытия файла в режиме для добавления текста
            password = self.password_entry.get()
            now_day = datetime.now()
            info = f"{password} {now_day.day}.{now_day.month}.{now_day.year}" \
                   f" {now_day.hour}:{now_day.minute}:{now_day.second} - {self.descriptions.get('1.0','end')}"
            #self.password(datetime.date.isoformat(datetime.date.today())) - это 28 строка от меня она оптемезирована как в книге
            password_file.write(info)
        self.save_password[password] = {f"{now_day.day}.{now_day.month}.{now_day.year} {now_day.hour}:{now_day.minute}:{now_day.second}":{self.descriptions.get('1.0','end')}}
        self.window.destroy()

    def get_date(self):
        i = 0
        for password, desk_and_date in self.save_password.items():
            if i == self.current_password:
                for date, desk in desk_and_date.items():
                    return date
            else:
                i = i + 1

    def get_description(self):
        i = 0
        for password, desk_and_date in self.save_password.items():
            if i == self.current_password:
                for date, desk in desk_and_date.items():
                    new_desk = ""
                    for i in range(len(str(desk))):
                        if i < 2 or i > len(str(desk))-2:
                            continue
                        else:
                            new_desk = new_desk + str(desk)[i]
                    return new_desk
            else:
                i = i + 1

    def get_password(self):
        i = 0
        for password, desk_and_date in self.save_password.items():
            if i == self.current_password:
                return password
            else:
                i = i + 1