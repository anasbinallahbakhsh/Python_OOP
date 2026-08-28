class person:
    count_instance=0
    def __init__(self,my_name,nick_name,):
        person.count_instance +=1
        self.my_name=my_name
        self.nick_name=nick_name
p1=person('Ans','ansy')
print(person.count_instance)
