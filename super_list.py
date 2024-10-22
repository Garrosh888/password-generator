class Supper_list(list):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.call_backs = []
    def  add_call_back(self,call_back):#функция добавления call_back в список (добавление и удалиние елементов списка)
        self.call_backs.append(call_back)
    def  append(self, value):#__setitem__  - метод для добавления елемента
        super(Supper_list, self).append(value)
        for call_back in self.call_backs:
            index = len(self) -1
            call_back(index,"set")
        print("set_item")

    def __delitem__(self, index):# __delitem__ - этот метод автоматически вызываеться при удалении елемента из списка
        super().__delitem__(index)
        print("pqweryui")
        for call_back in self.call_backs:
            call_back(index,"delete")
    def __setitem__(self, index, value):
        super(Supper_list, self).__setitem__(index,value)#super - обращение к родителю
        for call_back in self.call_backs:
            call_back(index,"edit")


