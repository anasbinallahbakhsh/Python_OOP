class phone:
    def __init__(self,brand,model_name,price):
        self.brand =brand 
        self.model_name=model_name
        self.price=price 
    def make_a_call(self,phone_number):
        print(f"calling {phone_number}...")
    def full_name(self):
        return f"{self.brand} {self.model_name}"
    def send_message(self):
        pass #twilia
phone2=phone('iphone','17 pro max',100000)

print(phone2.full_name())