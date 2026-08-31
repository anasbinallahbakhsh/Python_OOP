class person:

    count_instance = 0

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def from_string(cls, string):
        first, last, age = string.split(',')
        return cls(first, last, int(age))

    @classmethod
    def count_instance(cls):
        return f"You have created {cls.count_instance} instance of class name {cls.__name__}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_above_18(self):
        return self.age > 18


p1 = person('anas', 'malik', 17)

p2 = person.from_string('zohaib,solangi,18')