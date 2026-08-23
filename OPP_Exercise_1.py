class laptop:
    def __init__(self,brand_name,model_name,price):
        self.brand_name=brand_name
        self.model_name=model_name
        self.price=price
     
d1=laptop('chase_value', 'latest',10000)


print(d1.brand_name)
print(d1.model_name)
print(d1.price)