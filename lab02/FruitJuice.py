from Beverage import Beverage

class FruitJuice(Beverage):
    def __init__(self, ounces, price, fruits):
        Beverage.__init__(self, ounces, price)
        self.fruits = fruits # list of strings containing types of fruits

    def getInfo(self):
        return(f"{'/'.join(self.fruits)} Juice, {Beverage.getOunces(self)} oz, ${Beverage.getPrice(self):.2f}")
    
# juice = FruitJuice(16, 4.5, ["Apple", "Guava"])
# print(juice.getInfo())