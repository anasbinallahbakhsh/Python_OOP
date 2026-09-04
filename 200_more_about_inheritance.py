# can we derive more than one class from base class?
# multilevel inheritance
# method resolution order
# method overriding
# isinstance(), issubclass() functions


class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = price

    def make_a_call(self, number):
        return f"calling {number}...."


class Smartphone(Phone):  # derived / child class
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera):
        # two ways
        # Phone.__init__(self, brand, model_name, price)  # uncommon way

        super().__init__(brand, model_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

    def full_name(self):
        return f"{self.brand} {self.model_name} and price is {self._price}"


class FlagshipPhone(Smartphone):
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera, front_camera):
        super().__init__(brand, model_name, price, ram, internal_memory, rear_camera)
        self.front_camera = front_camera

    def full_name(self):
        return f"{self.brand} {self.model_name} and price is {self._price} and front_camera = {self.front_camera}"


smartphone = Smartphone('onePlus', '5', 30000, '6 GB', '64 GB', '20 MP')
oneplus = FlagshipPhone('onePlus', '9', 50000, '12 GB', '256 GB', '48 MP', '16 MP')






# print(smartphone.full_name())
# print(oneplus.full_name())
# print(oneplus.front_camera)
# print(help(FlagshipPhone))

# # isinstnace
# print(isinstance(oneplus, Phone))
# print(isinstance(oneplus, FlagshipPhone))

# issubclaspr
print(issubclass(smartphone, Phone))