class laptop:
     def __init__(self,brand_name,model,price):
      self.brand_name=brand_name
      self.model=model
      self.price=price
      self.laptop_name = brand_name + ' ' + model
     def apply_discount(self,percentage):
      discount=self.price*percentage /100
      return self.price -discount
laptop1=laptop('dell','core i six',4000)
print(laptop1.apply_discount(50))