class phone:
    def __init__(self, brand, model_name, price):
        self.brand=brand
        self.model_name=model_name
        self._price=max(price,0)
        self.complete_specification = f"{self.brand} {self.model_name} and for price {self._price}"

    def make_a_call(self,phone_number):
        print(f"calling {phone_number}")

    def full_name(self):
     return f"{self.brand}...{self.model_name}"




phone1=phone('oppo','A54',24000)
print(phone1.brand)
print(phone1.model_name)
print(phone1._price)
    