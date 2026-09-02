class Phone:
    def __init__(self, brand_name, model, price):
        self.brand_name = brand_name
        self.model = model
        self._price = max(price, 0)

    @property
    def complete_specification(self):
        return f"{self.brand_name} {self.model} and price is {self.price}"

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = max(value, 0)


    @price.setter
    def price(self,new_price):
        self._price = max(new_price,0)

    def make_a_call(self, phone_number):
        return f"{self.brand_name} {self.model} is calling {phone_number}"

    def full_name(self):
        return f"{self.brand_name} {self.model}"


phone1 = Phone('nokia', '1100', -1000)
phone1.price = 1000
print(phone1.price)
print(phone1.complete_specification)