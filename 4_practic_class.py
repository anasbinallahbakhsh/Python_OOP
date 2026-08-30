class Person:
    count_instance = 0

    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
@classmethod
def count_instsnce(cls):  
     return f"you have creted {count_instsnce} instnce of {__name__}"

def full_name(self):
        return f"{self.first_name} {self.last_name}"

def is_above_18(self):
        return self.age > 18


p1 = Person('anas', 'malik', 17)


