class phone:
    def __init__(self,model,brand_name,price):
        self,model=model
        self,brand_name=brand_name
        self,price=price 

    def make_a_call(self,phone_number):
        return f"{self.brand_name}{self.model}"
    def send_message(self):
        return f"Sending message from {self.brand_name} {self.model}"

phone2=phone('iphone','17 pro max',100000)
print(phone2.make_a_call('03087158286'))