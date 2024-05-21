import sqlite3
from password_info import Password_info
class save_sql_table():
    def __init__(self):
        self.connect = sqlite3.connect("data_base_password.db")  # execute - отправка запроса в базу данных
        self.cursor_object = self.connect.cursor()  # обьект для отправки запросов в базу данных


    def edit_table(self,id,new_password,new_description):
        self.cursor_object.execute(f"UPDATE table_password SET password = ? ,description = ? WHERE id = ?",(new_password,new_description,id))
        self.connect.commit()
    def delete_password(self,id):
        self.cursor_object.execute("DELETE FROM table_password WHERE id = ?",(id,))
        self.connect.commit()
    def printer(self):
        self.cursor_object.execute("SELECT * FROM table_password")
        passwords = self.cursor_object.fetchall()#получаем результат и записали в таблицу
        for i in passwords:
            print(i)
    def insert_data(self,password,description,date):
        self.cursor_object.execute("INSERT INTO table_password (password,description,date) VALUES (?, ?, ?)",(password,description,date))
        self.connect.commit()
    def create_table(self):
        self.cursor_object.execute("CREATE TABLE IF NOT EXISTS table_password(id INTEGER PRIMARY KEY,password TEXT,description TEXT,date TEXT )")

    def disconnect_data_base(self):
        self.connect.close()
    def get_info(self,save_passwords):
        self.cursor_object.execute("SELECT * FROM table_password")#ПОЛУЧАЮ ВСЮ ИНФОРМАЦИЮ
        all_passwords = self.cursor_object.fetchall()#получаем результат и записали в таблицу
        for i in all_passwords:
            id = i[0]
            password = i[1]
            descriptions = i[2]
            date = i[3]
            save_password_info = Password_info(id,password,descriptions,date)
            save_passwords.append(save_password_info)

password_list = []
object_save_sql_table = save_sql_table()
object_save_sql_table.get_info(password_list)
#object_save_sql_table.printer()
#object_save_sql_table.disconnect_data_base()

for i in password_list:
    print(i.id,i.password,i.description,i.date)
