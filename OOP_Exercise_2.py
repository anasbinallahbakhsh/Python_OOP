class laptop:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.name=model_name
        self.price=price
        self.laptop_name= brand+'', model_name
laptop=laptop('hp','au11tx',63000)
print(laptop.laptop_name)