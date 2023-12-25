from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza

class PizzaOrder(Pizza):
    def __init__(self, time):
        self.pizzas = []
        self.time = time
    
    def getTime(self):
        return self.time
    
    def setTime(self, time):
        self.time = time

    def addPizza(self, pizza):
        self.pizzas.append(pizza)

    def getOrderDescription(self):
        total_price = 0
        string = f"******\nOrder Time: {self.time}\n"
        for pizza in self.pizzas:
            string += f"{pizza.getPizzaDetails()}\n----\n"
            total_price += pizza.getPrice()
        string += f"TOTAL ORDER PRICE: ${total_price:.2f}\n******\n"
        return string

# cp1 = CustomPizza("S")
# cp1.addTopping("double cheese")
# cp1.addTopping("tomatoes")
# sp1 = SpecialtyPizza("S", "Cheesey")
# order = PizzaOrder(240001) #12:30:00PM
# order.addPizza(cp1)
# order.addPizza(sp1)

# cp2 = CustomPizza("L")
# cp2.addTopping("chicken")
# cp2.addTopping("onions")
# sp2 = SpecialtyPizza("M", "The UFO")
# # order = PizzaOrder(225659)
# order.addPizza(cp2)
# order.addPizza(sp2)

# print(order.getOrderDescription())