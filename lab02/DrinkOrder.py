from Beverage import Beverage
from Coffee import Coffee
from FruitJuice import FruitJuice

class DrinkOrder:
    def __init__(self):
        self.drinks = []

    def addBeverage(self, beverage):
        self.drinks.append(beverage)

    def getTotalOrder(self):
        string = ''
        price_total = 0
        string += "Order Items:\n"
        for bev in self.drinks:
            string += "* " + bev.getInfo() + "\n"
            price_total += (bev.getPrice())
        string += (f"Total Price: ${price_total:.2f}")
        return str(string)

c1 = Coffee(8, 3.0, "Espresso")
juice = FruitJuice(16, 4.5, ["Apple", "Guava"])
order = DrinkOrder()
order.addBeverage(c1)
order.addBeverage(juice)
print(order.getTotalOrder())