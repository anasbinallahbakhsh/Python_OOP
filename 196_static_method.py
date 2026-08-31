class Person:
    count_instance = 0

    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def from_string(cls, string):
        first, last, age = string.split(',')
        return cls(first, last, int(age))

    @classmethod
    def count_instances(cls):
        return f"you have created {cls.count_instance} instance of {cls.__name__}"

    @staticmethod
    def hello():
        print('hello, static method')

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_above_18(self):
        return self.age > 18


p1 = Person('anas', 'malik', 17)
p2 = Person.from_string('anas,malik,17')

print(p2.full_name())
print(p2.is_above_18())
print(Person.count_instances())
Person.hello()