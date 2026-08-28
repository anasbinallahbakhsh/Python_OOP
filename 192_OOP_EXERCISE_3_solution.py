class laptop:
     discount_percent=10
     def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self.price=price
        self.laptop_name = brand + " " + model_name
     def apply_discount(self):
        # self.price
       off_price=(laptop.discount_percent/100)*self.price
       return self.price - off_price
laptop.discount_percent=100
laptop1=laptop('dell','core,i,six', 63000)
laptop2=laptop('apple','macbook', 230000)
print(laptop2.apply_discount(50))