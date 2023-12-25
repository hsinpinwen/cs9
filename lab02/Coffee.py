from Beverage import Beverage

class Coffee(Beverage):
    def __init__(self, ounces, price, style):
        Beverage.__init__(self, ounces, price)
        
        # self.ounces = ounces
        
        # self.price = price
        self.style = style
    
    def getInfo(self):
        return(f"{self.style} Coffee, {Beverage.getOunces(self)} oz, ${Beverage.getPrice(self):.2f}")
    
# c1 = Coffee(8, 3.0, "Espresso")
# print(c1.getInfo())
# 'Espresso Coffee, 8 oz, $3.00'