from random import randint


class generate_password():
    def __init__(self):
        self.password = ""
        self.len_password = None
        self.numbers = "1234567890"
        self.letters = "qwertyuiopasdfghjklzxcvbnm"
        self.caps_letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
        self.symbols = "!#$%^&*()_+@}{:?></|\\,"
        self.users_symbols = ""
    def complite_user_symbols(self):
        self.users_symbols = input("введите символы для пароля \n")

    def generate_user_symbols_password(self):
        #self.len_password = len(self.users_symbols)
        use_index = []
        self.password = ""
        for i in range(self.len_password):#цикл длится столько раз сколько длина нашего пароля
            random_index = randint(0,len(self.users_symbols) -1)#random_index - случайный номер елемента из user_symbols для вставки в наш пароль
            if random_index in use_index:
                while random_index in use_index:
                    random_index = randint(0,len(self.users_symbols) -1)
                self.password += self.users_symbols[random_index]
                use_index.append(random_index)
            else:
                self.password += self.users_symbols[random_index]
                use_index.append(random_index)

    def set_len_password(self):#просто просим ввести пользователя длину пароля
        print("введите длину пароля")
        self.len_password = int(input())

    def generate_one_type_password(self,stroka):
        self.password = ""
        for i in range(self.len_password):
            index_number = randint(0, len(stroka) - 1)
            self.password += stroka[index_number]
        print(self.password)
    def generate_password_two_types(self,str1,str2):
        self.password = ""
        for i in range(self.len_password):
            value = randint(1,2)
            if value == 1:
                self.password += str1[randint(0,len(str1)-1)]
            elif value == 2:
                self.password += str2[randint(0, len(str2) - 1)]
        print(self.password)

    def generate_password_three_types(self,str1,str2,str3):
        self.password = ""
        for i in range(self.len_password):
            value = randint(1,3)
            if value == 1:
                self.password += str1[randint(0,len(str1)-1)]
            elif value == 2:
                self.password += str2[randint(0, len(str2) - 1)]
            elif value == 3:
                self.password += str3[randint(0, len(str3) - 1)]
        print(self.password)

    def generate_password_hard(self):
        self.password = ""
        for i in range(self.len_password):
            value = randint(1,4)
            if value == 1:
                self.password += self.numbers[randint(0,len(self.numbers)-1)]
            elif value == 2:
                self.password += self.letters[randint(0, len(self.letters) - 1)]
            elif value == 3:
                self.password += self.caps_letters[randint(0, len(self.caps_letters) - 1)]
            elif value == 4:
                self.password += self.symbols[randint(0, len(self.symbols) - 1)]
        print(self.password)


#password_by_aziz = generate_password()
#password_by_aziz.complite_user_symbols()
#password_by_aziz.generate_user_symbols_password()
#print(password_by_aziz.password)
