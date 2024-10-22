from tkinter import*
from generate_password import generate_password
import time
#import pyperclip
from super_list import Supper_list
from datetime import datetime
from descriptions_for_password import Description
from save_my_new_password import Description_from_me
from SQL_database import save_sql_table
from edit_password import Edit_password

def change_password():
    id = example_for_tk_from_SQL_database.get_id(get_password(),get_description(),get_date())
    object_Edit_password = Edit_password(save_passwords,example_for_tk_from_SQL_database,id,current_password)





def get_all_info():
    if current_password < 0:
        text_password_description_date.insert(END,"у вас нету сохраненных паролей")
    text = f"{get_password()}\n\n{get_description()}\n\n{get_date()}"
    text_password_description_date.insert(END,text)
def complite_new_passwor():
    Description_from_me(save_passwords,example_for_tk_from_SQL_database)


def call_back(index,action):#call_back - это функция вызываеться кажды раз когда мы убераем или добовляем елемент в словарь
    global current_password
    if action == "set":
        current_password = current_password + 1
    elif action == "delete":
        if current_password > 0:
            current_password = current_password - 1
        else:
            if  len(save_passwords) == 0:
                current_password = -1
    elif action == "edit":
        pass

    text_password_description_date.configure(state="normal")
    text_password_description_date.delete(1.0,END)

    get_all_info()
    text_password_description_date.configure(state="disabled")

def click_delete_password():
    if current_password < 0:
        print("нету пароля")
        get_all_info()
        return
    id = save_passwords[current_password].id
    del save_passwords[current_password]#del - метод для удаления елемента из  словаря
    example_for_tk_from_SQL_database.delete_password(id)



def get_date():
    if current_password == -1:
        return ""
    return save_passwords[current_password].date
def get_description():
    if current_password == -1:
        return ""
    return save_passwords[current_password].description

def btn_back_current_password(event):
    global current_password
    if current_password > 0:
        current_password = current_password - 1
        text_password_description_date.configure(state="normal")
        text_password_description_date.delete(1.0,END)
        get_all_info()
        text_password_description_date.configure(state="disabled")
    print(current_password)
def btn_next_current_password(event):
    global current_password
    if current_password < len(save_passwords) -1:#- save_passwords.items() - items() это елементы словоря
        current_password = current_password + 1
        text_password_description_date.configure(state="normal")
        text_password_description_date.delete(1.0,END)
        get_all_info()
    text_password_description_date.configure(state="disabled")
    print(current_password)

def get_password():
    if current_password == -1:
        return ""
    return save_passwords[current_password].password

def click_btn_description(event):
    global description_is_open
    if description_is_open == False:
        description_is_open = True
        cnv.itemconfigure(button_descriptions,image = img_btn_for_descriptions_grey)
        window.geometry("950x500")
        cnv.update()
        cnv.update_idletasks()
        time.sleep(0.2)
        cnv.itemconfigure(button_descriptions, image=img_btn_for_descriptions_black)
    else:
        description_is_open = False
        cnv.itemconfigure(button_descriptions,image= img_btn_for_descriptions_grey)
        window.geometry("700x500")
        cnv.update()
        cnv.update_idletasks()
        time.sleep(0.2)
        cnv.itemconfigure(button_descriptions, image=img_btn_for_descriptions_black)
def click_save(event):
    global current_password
    if len(entry_password.get()) == 0:
        return
    else:
        Description(entry_password.get(),save_passwords,example_for_tk_from_SQL_database)
        cnv.itemconfigure(button_save, image=img_save_grey)#изменения свойства image у елемента button_save
        #itemconfigure - изменяет свойство елемента на канве
        cnv.update()#обнавляет канву
        cnv.update_idletasks()#обнавляет елементы на канве
        time.sleep(0.2)
        cnv.itemconfigure(button_save, image=img_save_black)


def click_copy(event):
    if len(entry_password.get()) == 0:
        return
    else:
       # pyperclip.copy(entry_password.get())
        cnv.itemconfigure(button_copy,image = img_copy_grey)
        cnv.update()
        cnv.update_idletasks()
        time.sleep(0.2)
        cnv.itemconfigure(button_copy, image=img_copy_black)

def click_musorka(event):
    global permission_for_entr_password
    entr1.delete(0,END)
    entr2.delete(0,END)
    permission_for_entr_password = True
    entry_password.delete(0, END)
    permission_for_entr_password = False
    btn1["bg"] = "grey"
    btn2["bg"] = "grey"
    btn3["bg"] = "grey"
    btn4["bg"] = "grey"
    btn5["bg"] = "grey"

def click_btns(btn,type_symbols):
    global  is_symbols,is_numbers,is_letters,is_caps_letters
    value = True
    if btn["bg"] == "grey":
        btn["bg"] = "green"
        value = True
    elif btn["bg"] == "green":
        btn["bg"] = "grey"
        value = False
    if type_symbols == "numbers":
        is_numbers = value
    elif type_symbols == "symbols":
        is_symbols = value
    elif type_symbols == "letters":
        is_letters = value
    elif type_symbols == "caps_letters":
        is_caps_letters = value

def click_generate_password():#функция выполняется на желтую кнопку сгенерировать
    global permission_for_entr_password
    global is_user_symbols, is_numbers, is_letters, is_caps_letters, is_symbols, is_dublicate
    if is_correct == False:
        return
    generator = generate_password()
    if len(entr1.get()) >= 4 and len(entr1.get()) <= 24 and entr1["fg"] != "#757575":
        generator.len_password = len(entr1.get())
    else:
        generator.len_password = int(entr2.get())
    if entr1["fg"] != "#757575":
        generator.users_symbols = entr1.get()
        generator.generate_user_symbols_password()
    else:
        value_list = []
        if is_numbers == True:
            value_list.append(generator.numbers)
        if is_letters == True:
            value_list.append(generator.letters)
        if is_caps_letters == True:
            value_list.append(generator.caps_letters)
        if is_symbols == True:
            value_list.append(generator.symbols)
        if len(value_list) == 4:
            generator.generate_password_hard()
        elif len(value_list) == 1:
            generator.generate_one_type_password(value_list[0])
        elif len(value_list) == 2:
            generator.generate_password_two_types(value_list[0],value_list[1])
        elif len(value_list) == 3:
            generator.generate_password_three_types(value_list[0],value_list[1],value_list[2])

    permission_for_entr_password = True#permission - разришение
    entry_password.delete(0, END)
    entry_password.insert(0, generator.password)
    permission_for_entr_password = False


def focus_in_entr1(event):#удаление подскаски когда елемент в фокуси(когда наш курсор там)
    if entr1["fg"] == "#757575":
        entr1.delete(0,END)

def focus_out_entr1(event):#добавление подсказки когда елемент не в фокусе и пользователь ничего не ввел
    if len(entr1.get()) == 0:
        entr1["fg"] = "#757575"
        entr1.insert(0,"4-24 символа")

def change_galocka(event):
    global use_user_symbols#это показатель что используем символ из entr1
    check_data()#выозов функции
    if is_correct == True:
        cnv_for_galochka.itemconfigure(img_galocka,image = img_zelenaa_galochka)
        save_settings()
    else:
        cnv_for_galochka.itemconfigure(img_galocka, image = img_red_galochka)

def save_settings():
    global is_user_symbols,is_numbers,is_letters,is_caps_letters,is_symbols,is_dublicate
    is_user_symbols = True
    is_numbers = False
    is_letters = False
    is_caps_letters = False
    is_symbols = False
    is_dublicate = False
    if len(entr1.get()) == 0 or entr1["fg"] == "#757575":#⬇⬇️⬇ ️
        is_user_symbols = False
        if btn1["bg"] == "green":
            is_numbers = True
        else:
            btn1["bg"] = "red"
        if btn2["bg"] == "green":
            is_letters = True
        else:
            btn2["bg"] = "red"
        if btn3["bg"] == "green":
            is_caps_letters = True
        else:
            btn3["bg"] = "red"
        if btn4["bg"] == "green":
            is_symbols = True
        else:
            btn4["bg"] = "red"
        if btn5["bg"] == "green":
            is_dublicate = True
        else:
            btn5["bg"] = "red"

    if is_user_symbols == True:

        entr2.delete(0,END)
        entr2.insert(0,str(len(entr1.get())))#заполнение поля длины пароля(будет в том случае если пользователь не указал сам длину пароля)

        symbols = entr1.get()

        copy_user_symbols = []
        for i in symbols:
            if i.isdigit() == True:
                is_numbers = True
            for letter in object_generate_password.letters:
                if letter == i:
                    is_letters = True
                    break
            for letter in object_generate_password.caps_letters:
                if letter == i:
                    is_caps_letters = True
                    break
            for letter in object_generate_password.symbols:
                if letter == i:
                    is_symbols = True
                    break
            if i in copy_user_symbols:
                is_dublicate = True
            else:
                copy_user_symbols.append(i)
        print(copy_user_symbols)
        if is_numbers == True:
            btn1["bg"] = "green"
        else:
            btn1["bg"] = "red"
        if is_letters == True:
            btn2["bg"] = "green"
        else:
            btn2["bg"] = "red"
        if is_caps_letters == True:
            btn3["bg"] = "green"
        else:
            btn3["bg"] = "red"
        if is_symbols == True:
            btn4["bg"] = "green"
        else:
            btn4["bg"] = "red"
        if is_dublicate == False:
            btn5["bg"] = "green"
        else:
            btn5["bg"] = "red"


def validate_entr1(text):#валидация на галочку на сохранение измения
    global is_correct
    #is_correct = False
    if len(text) == 0 or text == "4-24 символа":
        entr1["fg"] = "#757575"
    else:
        entr1["fg"] = "black"
    if len(text) < 4:
        cnv_for_galochka.itemconfigure(img_galocka,image = img_red_galochka)#itemconfigure - это изминение свойства у элемента на канве
    return validate_length_pass_entr1(text)


def validate_length_pass_entr2(text):#validate это правило ,в данном примере правила ввода длины пароля
    global is_correct
    #is_correct = False
    #cnv_for_galochka.itemconfigure(img_galocka, image=img_red_galochka)
    if len(text) == 0:
        return True
    if len(text) >2:
        return  False
    if text.isdigit() and int(text) > 24:
        return False
    return text.isdigit()#isdigit - проверка является ли текст числом

def validate_length_pass_entr1(text):#validate это правило ,в данном примере правила ввода длины пароля
    if len(text) > 24:
        return False
    else:
        return True
def validate_paste_password_entr(text):
    return permission_for_entr_password#это проверка entr_password запрет ввода туда символов


def check_data():#проверка что пользвателем введено не более 24 символов
    global is_correct
    if len(entr1.get()) >= 4 and len(entr1.get()) <= 24 and entr1['fg'] == "black":
        is_correct = True
    elif  int(entr2.get()) >= 4 and int(entr2.get()) <= 24:
        if btn1["bg"] == "green" or btn2["bg"] == "green" or btn3["bg"] == "green" or btn4["bg"] == "green":
            is_correct = True
        else:
            is_correct = False
    else:
        is_correct = False

save_passwords = Supper_list()
data = None#переменная для хронения всей информации из  файла с паролями

example_for_tk_from_SQL_database = save_sql_table()#создаем екземпляр save_sql_table
example_for_tk_from_SQL_database.get_info(save_passwords)#заполнение списка save_passwods из базы данных

for i in save_passwords:
    print(i.password,i.description)
example_for_tk_from_SQL_database = save_sql_table()
description_is_open = False
description = None
save_passwords.add_call_back(call_back)
use_user_symbols= True#значение False символа для пароля генерируются програмой,значение True когда используються символы ввиденые пользователем
window = Tk()
window.resizable(0,0)
window.iconbitmap("s2.ico")
window.title("password from sfit")
window.geometry("700x500")
cnv = Canvas(window,width = 950,height=500,bg="#afdec2")
cnv.place(x=0,y=0)
cnv.create_line(705,0,705,500,width=5)
img_musorka = PhotoImage(file="musur_bag_s_chelovechkom.png")
musorka =cnv.create_image(500,10,anchor = NW,image = img_musorka)
img_copy_black = PhotoImage(file="copy_black.png")
img_copy_grey = PhotoImage(file="copy_grey.png")
img_save_black = PhotoImage(file="save_black.png")
img_save_grey = PhotoImage(file="save_grey.png")
img_btn_for_descriptions_black = PhotoImage(file="descriptions_for_password_black.png")
img_btn_for_descriptions_grey = PhotoImage(file="descriptions_for_password_grey.png")
img_back = PhotoImage(file="strela_levo.png")
img_next = PhotoImage(file="strela_pravo.png")
button_copy = cnv.create_image(600,15,anchor= NW,image =img_copy_black)
button_save = cnv.create_image(600,120,anchor= NW,image= img_save_black)
button_descriptions = cnv.create_image(600,220,anchor= NW,image = img_btn_for_descriptions_black)

button_back = cnv.create_image(715,400,anchor=NW,image=img_back)
button_next = cnv.create_image(900,400,anchor=NW,image=img_next)
cnv.tag_bind(button_copy,"<Button-1>",click_copy)
cnv.tag_bind(musorka,"<Button-1>",click_musorka)
cnv.tag_bind(button_save,"<Button-1>",click_save)
cnv.tag_bind(button_descriptions,"<Button-1>",click_btn_description)
cnv.tag_bind(button_next,"<Button-1>",btn_next_current_password)
cnv.tag_bind(button_back,"<Button-1>",btn_back_current_password)
cnv_for_galochka = Canvas(cnv,width=25,height=25,bg="#afdec2")
cnv_for_galochka.place(x=50, y=300)


regester_validate_entr1 = window.register(validate_entr1)#регестрация функции для валидации
object_generate_password = generate_password()
permission_for_entr_password = False#permission - разришение
regester_validate_paste_password_entr = window.register(validate_paste_password_entr)
is_user_symbols = True
is_numbers = False
is_letters = False
is_caps_letters = False
is_symbols = False
is_dublicate = False
current_password = len(save_passwords) -1
print(current_password)
#all btns
x_btn = 330
btn1 = Button(cnv,text="Цифры",font=(None,20),bg= "grey",fg= "black")
btn1.place(x = x_btn ,y= 30 )
btn2 = Button(cnv,text="Маленькие буквы",font=(None,20),bg= "grey",fg= "black")
btn2.place(x = x_btn ,y= 130 )
btn3 = Button(cnv,text="Заглавные буквы",font=(None,20),bg= "grey",fg= "black")
btn3.place(x = x_btn ,y= 230 )
btn4 = Button(cnv,text="Специальные символы",font=(None,20),bg= "grey",fg= "black")
btn4.place(x = x_btn ,y= 330 )
btn5 = Button(cnv,text="Исключать похожие символы",font=(None,19),bg= "grey",fg= "black")
btn5.place(x = x_btn,y= 430 )
btn6 = Button(cnv,text="Сгенерировать",font=(None,20),bg= "gold",fg= "black",command=click_generate_password)
btn6.place(x = 40 ,y =330 )
btn_delete = Button(cnv, text="удалить этот пароль", font=(None,10), fg="red", command=click_delete_password)
btn_delete.place(x= 763,y= 450)
btn_complite_newpass = Button(cnv,text="добавть свой пароль",font=(None,10),fg="green",command=complite_new_passwor)
btn_complite_newpass.place(x=762,y =30)
btn_change = Button(cnv,text="изменить пароль и описание",font=(None,10),fg="green",command= change_password)
btn_change.place(x=738,y =370)
#подключение функции на событие нажатие на кнопки
btn1.bind("<Button-1>",lambda event: click_btns(btn1,"numbers"))#lambda - нужна для передачи функции параметра
btn2.bind("<Button-1>",lambda event: click_btns(btn2,"letters"))
btn3.bind("<Button-1>",lambda event: click_btns(btn3,"caps_letters"))
btn4.bind("<Button-1>",lambda event: click_btns(btn4,"symbols"))
btn5.bind("<Button-1>",lambda event: click_btns(btn5,"no_some_similar_symbols"))
#all entr
entr1 = Entry(cnv,font=(None,17),fg = "#757575",width=24,validate= "key",validatecommand= (regester_validate_entr1,"%P"))
entr1.place(x= 5,y = 130)#  %P  = текст из елемента entr1
entr1.insert(0,"4-24 символа")#insert это - вставка текста
entr1.bind("<FocusIn>",focus_in_entr1)
entr1.bind("<FocusOut>",focus_out_entr1)
validate = window.register(validate_length_pass_entr2)#регестрируем функцию как валидацию
entr2 = Entry(cnv,font=(None,20),width = 2,validate = "key",validatecommand= (validate,"%P"),)#
entr2.place(x= 5,y = 30)
entr2.focus_set()
entry_password = Entry(cnv, font=(None, 18), width=24, validate="key", validatecommand=(regester_validate_paste_password_entr, "%P"))
entry_password.place(x = 5, y = 400)


#all text
cnv.create_text(5,111,text="Генерировать из символов:",anchor=NW)
cnv.create_text(10,170,text="4-24 символа",anchor=NW)
cnv.create_text(80,300,text="сохранить изменения",anchor=NW)
cnv.create_text(5,10,text="количество символов от 4 до 24",anchor=NW)
text_warning = cnv.create_text(400,480,text="актуально только со своими символами",anchor=NW,font=(None,10))
text_password_description_date = Text(cnv,width=30,height=15,font=(None,10),wrap = "word",padx=5,pady = 5)
get_all_info()
text_password_description_date.place(x= 717,y= 100)
text_password_description_date.configure(state="disabled")


img_zelenaa_galochka = PhotoImage(file="zelenaa_galochka.png")
img_red_galochka = PhotoImage(file ="red_galochka.png")
img_galocka = cnv_for_galochka.create_image(2, 1, anchor = NW, image = img_red_galochka)#⬇
#создание изображения с именем img_galocka на канве с свойством image = img_belaa_galochka
cnv_for_galochka.tag_bind(img_galocka,"<Button-1>",change_galocka)

is_correct = False#показатель коректные ли даннные в програме(4 - 24 символов)





window.mainloop()


