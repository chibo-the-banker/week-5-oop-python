""" Question 1: Class Smartphone with the following attributes:"""
class Smartphone:
    def __init__(self, color,brand, security):
        self.color=color
        self.brand=brand
        self.security=security

    def buy(self):
        if self.security==True:
            return f"Your {self.brand} smartphone is secure and safe to buy."
        else:
            return f"Your {self.brand} smartphone is not safe to buy."
        
    def charger(self):
        if self.brand=="Apple":
            return f"Your {self.brand} smartphone is expensive and not easy to replace."
        else:
            return f"Your {self.brand} smartphone is affordable and easier to replace."
phone=Smartphone("pink", "apple", True)
print(phone.buy())

""" Question 2""" 
class Car:
    def move(self):
        return "The car is driving."
    
class plane:
    def move(self):
        return "The plane is flying."
    
class spacecraft:
    def move(self):
        return "The spacecraft is orbiting."
    
print(Car().move())
print(plane().move())   