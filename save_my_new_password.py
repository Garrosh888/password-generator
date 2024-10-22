from tkinter import *
from datetime import datetime
from password_info import Password_info
class Description_from_me():
    def  __init__(self,save_password,table_sql):
        self.create_window()
        self.save_password = save_password
        self.table_sql = table_sql
    def create_window(self):
        self.window = Tk()
        self.window.resizable(0, 0)
        self.window.iconbitmap("S2A_icona.ico")
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
        now_day = datetime.now()
        description = self.descriptions.get('1.0', 'end')  # получение описания к паролю
        date = f"{now_day.day}.{now_day.month}.{now_day.year} {now_day.hour}:{now_day.minute}:{now_day.second}"
        password = self.password_entry.get()
        self.table_sql.insert_data(password, description, date)
        id = self.table_sql.get_id(password, description, date)
        password_info = Password_info(id,password, description, date)
        self.save_password.append(password_info)
        self.window.destroy()
