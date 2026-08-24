class laptop:

    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand + ' ' + model_name

    def apply_discount(self, percentage):
        discount = self.price * percentage / 100
        return self.price - discount


laptop1 = laptop('hp', 'core i6 gen', 9000)

print(laptop1.apply_discount(20))