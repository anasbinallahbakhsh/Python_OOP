class laptop:
    def __init__(self,brand_name,model_name,price):
        self.brand_name=brand_name
        self.model_name=model_name
        self.price=price
        self.laptop_name= brand_name + "", model_name
     
data=laptop('chase_value', 'latest',10000)
laptop.apply_diccount(40)


