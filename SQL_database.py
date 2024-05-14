import sqlite3
def delete_password(id):
    cursor.execute("DELETE FROM table_password WHERE id = ?",(id,))
    connect.commit()
def printer():
    cursor.execute("SELECT * FROM table_password")
    passwords = cursor.fetchall()
    for i in passwords:
        print(i)
def insert_data(password,description,date):
    cursor.execute("INSERT INTO table_password (password,description,date) VALUES (?, ?, ?)",(password,description,date))
    connect.commit()
def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS table_password(id INTEGER PRIMARY KEY,password TEXT,description TEXT,date TEXT )")
connect = sqlite3.connect("data_base_password.db")#execute - отправка запроса в базу данных

cursor = connect.cursor()#обьект для отправки запросов в базу данных

create_table()
#insert_data("12345","hello","14.05.2024")
#insert_data("56789","good bye","14.05.2024")
#insert_data("11121","hello","14.05.2024")
#delete_password(2)
printer()
connect.close()