from tkinter import *
from SQL_database import save_sql_table
from datetime import datetime
from password_info import Password_info
class Description():
    def  __init__(self,password,save_password,table_sql):
        self.password = password
        self.create_window()
        self.save_password = save_password
        self.table_sql = table_sql

    def create_window(self):
        self.window = Tk()
        self.window.resizable(0, 0)
        self.window.iconbitmap("s2.ico")
        self.window.title("sftc")
        self.cnv = Canvas(self.window, width=300, height=200,bg="#afdec2")
        self.cnv.pack()
        self.cnv.create_text(70, 10, anchor=NW, text="введите описание", font=(None, 15))
        self.descriptions = Text(self.cnv, font=(None, 10), width=30, height=5)
        self.descriptions.place(x=40, y=50)
        self.save_btn = Button(self.cnv, text="save", font=(None, 15),bg= "green",command=self.click_save)
        self.save_btn.place(x=40, y=150)
        self.cancel_btn = Button(self.cnv, text="cancel", font=(None, 15),bg="red", command=self.click_cancel)
        self.cancel_btn.place(x=180, y=150)
        #window.mainloop()
    def click_cancel(self):
        self.window.destroy()

    def click_save(self):
        now_day = datetime.now()
        description = self.descriptions.get('1.0', 'end')#получение описания к паролю
        date = f"{now_day.day}.{now_day.month}.{now_day.year} {now_day.hour}:{now_day.minute}:{now_day.second}"
        self.table_sql.insert_data(self.password,description,date)
        id = self.table_sql.get_id(self.password,description,date)
        password_info = Password_info(id,self.password,description,date)
        self.save_password.append(password_info)
        self.window.destroy()




