class  person:
    count_instance=0
    def __init__(self,first_naem,last_name,age):
        person.count_instance +=1
        self.first_name=first_naem
        self.last_name=last_name
        self.age=age

p1=person('anas','nasy',17)
p1=person('anas','nasy',17)     
p1=person('anas','nasy',17)
print(person.count_instance)

