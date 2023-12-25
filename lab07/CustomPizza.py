from Pizza import Pizza

class CustomPizza(Pizza):
    def __init__(self, size):
        Pizza.__init__(self, size)
        self.toppings = []
        if size == "S":
            self.price = 8.00
        elif size == "M":
            self.price = 10.00
        elif size == "L":
            self.price = 12.00

    def addTopping(self, topping):
        if topping != []:
            if self.size == "S":
                self.price += 0.50
                self.toppings.append(topping)
            elif self.size == "M":
                self.price += 0.75
                self.toppings.append(topping)
            elif self.size == "L":
                self.price += 1.00
                self.toppings.append(topping)

    def getPizzaDetails(self):
        string = f'CUSTOM PIZZA\nSize: {self.size}\nToppings:\n'
        for top in self.toppings:
            string += "\t+ " + top + "\n"
        string += f"Price: ${self.price:.2f}\n"
        return string
    
# cp1 = CustomPizza("S")

# assert cp1.getPizzaDetails() == \
# "CUSTOM PIZZA\n\
# Size: S\n\
# Toppings:\n\
# Price: $8.00\n"

# cp1 = CustomPizza("L")
# cp1.addTopping("extra cheese")
# cp1.addTopping("sausage")

# assert cp1.getPizzaDetails() == \
# "CUSTOM PIZZA\n\
# Size: L\n\
# Toppings:\n\
# \t+ extra cheese\n\
# \t+ sausage\n\
# Price: $14.00\n"

# cp2 = CustomPizza("M")
# cp2.addTopping("anchovies")
# cp2.addTopping("jelly beans")
# cp2.addTopping("bananas")
# print(cp2.getPizzaDetails())