class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self._price = max(price, 0)

    @property
    def complete_specification(self):
        return f"{self.brand} {self.model} and price is {self.price}"

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        self._price = max(new_price, 0)

    def make_a_call(self, phone_number):
        print(f"calling {phone_number}")


phone1 = Phone('Tecno', 'spark go 2', 25000)
phone1.price = 90
print(phone1.brand)
print(phone1.model)
print(phone1.complete_specification)