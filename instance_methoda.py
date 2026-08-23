#Instance method
class person:
    def __init__(self,first_name,last_name,age):
       self.first_name = first_name
       self.last_name = last_name
       self.age=age
    def full_mame(self):
        return (f"{self.first_name},{self.last_name}")
    def is_above_18(self):
        return self.age>18 

p1=person('Anas','Malik',19)
p2=person('Ana','Malik',10)

print(p1.is_above_18())

# print(p1.full_mame)
l=[1,2,3,4,]
#clear ,pop
# list.clear(l)
# print(l)
# list.append(9)
list.append(l,10)
print(l)