class Supper_dict(dict):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.call_backs = []
    def  add_call_back(self,call_back):
        self.call_backs.append(call_back)
    def  __setitem__(self, key, value):#__setitem__  в блокноте
        super(Supper_dict, self).__setitem__(key,value)
        for call_back in self.call_backs:
            call_back(key,value,"set")
    def __delitem__(self, key):#этот метод автоматически вызываеться при удалении елемента из словаря
        value = self[key]
        super().__delitem__(key)
        for call_back in self.call_backs:

            call_back(key,value,"delete")
