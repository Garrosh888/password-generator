from tkinter import *
from SQL_database import save_sql_table
from password_info import Password_info

class Edit_password():
    def __init__(self,save_password,table_sql,id,current_password):
        self.save_passwords = save_password
        self.table_sql = table_sql
        self.id = id
        self.create_window()
        self.current_password = current_password
    def create_window(self):
        self.window = Tk()
        self.window.resizable(0, 0)
        self.window.iconbitmap("s2.ico")
        self.window.title("sftc")
        self.cnv = Canvas(self.window, width=300, height=300, bg="#afdec2")
        self.cnv.pack()
        self.cnv.create_text(25, 10, anchor=NW, text="пароль для редактирования", font=(None, 15))
        self.password_entry = Entry(self.cnv, font=(None, 10), width=30)
        self.password_entry.place(x=40, y=50)
        self.password_entry.insert(0,self.table_sql.get_password(self.id))
        self.cnv.create_text(20, 75, anchor=NW, text="описание для редактирования", font=(None, 15))
        self.descriptions = Text(self.cnv, font=(None, 10), width=30, height=5 )
        self.descriptions.place(x=40, y=110)
        self.descriptions.insert(END,self.table_sql.get_description(self.id))
        self.save_btn = Button(self.cnv, text="save", font=(None, 15), bg="green", command=self.click_save)
        self.save_btn.place(x=40, y=225)
        self.cancel_btn = Button(self.cnv, text="cancel", font=(None, 15), bg="red", command=self.click_cancel)
        self.cancel_btn.place(x=180, y=225)
    def click_cancel(self):
        self.window.destroy()

    def click_save(self):
        edit_password = self.password_entry.get()
        if len(edit_password) == 0:
            return
        edit_description =self.descriptions.get('1.0', 'end')
        date = self.save_passwords[self.current_password].date
        self.table_sql.edit_table(self.id,edit_password,edit_description)
        example_password_info = Password_info(self.id,edit_password,edit_description,date)
        example_password_info.change = True
        self.save_passwords[self.current_password] =  example_password_info
        self.window.destroy()

