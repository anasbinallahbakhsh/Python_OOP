# OBJECTIVE

# WHAT IS CLASS

# HOW TO CREATE A CLASS

# WHAT IS INIT METHOD

# WHAT ARE ATTRIBUTES, INSTANCE

# HOW TO CREATE OUR OBJECT


class Person:

    def __init__(self, first_name, last_name, age):

        # instance variables
        print('init method // constructor get called')

        self.first_name = first_name
        self.last_name = last_name
        self.age = age


p1 = Person('anas', 'malik', 17)

# p2 = Person('zohaib', 'solangi', 17)


print(p1.first_name)

# print(p1.first_name)