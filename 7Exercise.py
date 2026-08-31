class person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def count_instances(cls):
        return f"You have created {cls.count_instances} of person class"

    def full_name(self):
        return f"{self.first_name}, {self.last_name}"

    def is_above_18(self):

 
     p1 = person('anas', 'malik', 17)

     p2 = person('zohaib', 'solangi', 19)

print(person.count_instances())