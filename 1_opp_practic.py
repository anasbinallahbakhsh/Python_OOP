class  person:
    def __init__(self,my_name,my_nick_name,age):
        self.my_name=my_name
        self.my_nick_name=my_nick_name
        self.age=age
    def is_above_19(self):
        return self.age>19

my_data=person('anas','malik',19)
print(my_data.is_above_19())