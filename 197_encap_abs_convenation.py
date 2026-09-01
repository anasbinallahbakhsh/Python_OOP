# Encapsulation and Abstraction

# abstract class

# name mangling, __name (convention of private name), __name__ (dunder/magic name convention of python)

class Phone:

    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self.__price = price
    def make_a_call(self, phone_number):
        print(f"calling {phone_number}...")
    def full_name(self):
        return f"{self.brand} {self.model_name}"
    def send_message(self):
        pass  # twilio
phone1 = Phone('nokia', '1100', 1001)
# print(phone1._Phone__price)
phone1._Phone__price = -1001
print(phone1._Phone__price)
# print(phone1.__dict__)
l = [1, 3, 9, 2, 4, 4, 2, 2, 4, 2, 4]
l.sort()  # tim sort
print(l)