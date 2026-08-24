class laptop:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self.price=price
        self.laptop_name = brand + " " + model_name
    def apply_discount(self,num):
        # self.price
       off_price=(num/100)*self.price
       return self.price - off_price
laptop5=laptop('dell','core,i,six', 8000)

laptop2=laptop('apple','macbook', 20000)

print(laptop2.apply_discount(50))