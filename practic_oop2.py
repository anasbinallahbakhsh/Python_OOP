class laptop:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
        self.laptop_name=brand+'' , model +''
    def apply_discount(self,percentage):
         discount=self.price*percentage /100
         return self.price - discount
laptop4=laptop('hp','i six', 500)
print(laptop4.apply_discount(50))