class Supper_list(list):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.call_backs = []
    def  add_call_back(self,call_back):#функция добавления call_back в список (добавление и удалиние елементов списка)
        self.call_backs.append(call_back)
    def  __setitem__(self, index, value):#__setitem__  - метод для добавления елемента
        super(Supper_list, self).__setitem__(index, value)
        for call_back in self.call_backs:
            call_back(index,"set")
    def __delitem__(self, index):# __delitem__ - этот метод автоматически вызываеться при удалении елемента из списка
        super().__delitem__(index)
        for call_back in self.call_backs:

            call_back(index,"delete")
