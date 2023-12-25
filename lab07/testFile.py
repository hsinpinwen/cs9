from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from PizzaOrder import PizzaOrder
from OrderQueue import OrderQueue

def test_CustomPizza():
    cp1 = CustomPizza("S")

    assert cp1.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
Price: $8.00\n"
    cp1 = CustomPizza("L")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")

    assert cp1.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: L\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $14.00\n"
    cp2 = CustomPizza("M")
    cp2.addTopping("anchovies")
    cp2.addTopping("jelly beans")
    cp2.addTopping("bananas")
    assert cp2.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: M\n\
Toppings:\n\
\t+ anchovies\n\
\t+ jelly beans\n\
\t+ bananas\n\
Price: $12.25\n"
    cp2.addTopping("mushrooms")
    assert cp2.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: M\n\
Toppings:\n\
\t+ anchovies\n\
\t+ jelly beans\n\
\t+ bananas\n\
\t+ mushrooms\n\
Price: $13.00\n"

def test_SpecialtyPizza():
    sp1 = SpecialtyPizza("S", "Carne-more")
    assert sp1.getPizzaDetails() == \
"SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n"
    sp2 = SpecialtyPizza("M", "Meat Lovers")
    assert sp2.getPizzaDetails() == \
"SPECIALTY PIZZA\n\
Size: M\n\
Name: Meat Lovers\n\
Price: $14.00\n"
    sp3 = SpecialtyPizza("L", "Calzone")
    assert sp3.getPizzaDetails() == \
"SPECIALTY PIZZA\n\
Size: L\n\
Name: Calzone\n\
Price: $16.00\n"

def test_PizzaOrder():
    cp1 = CustomPizza("S")
    cp1.addTopping("double cheese")
    cp1.addTopping("tomatoes")
    sp1 = SpecialtyPizza("S", "Cheesey")
    order = PizzaOrder(240001) #12:30:00PM
    order.addPizza(cp1)
    order.addPizza(sp1)

    assert order.getOrderDescription() == \
"******\n\
Order Time: 240001\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ double cheese\n\
\t+ tomatoes\n\
Price: $9.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Cheesey\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $21.00\n\
******\n"

    cp2 = CustomPizza("L")
    cp2.addTopping("chicken")
    cp2.addTopping("onions")
    sp2 = SpecialtyPizza("M", "The UFO")
    # order = PizzaOrder(225659)
    order.addPizza(cp2)
    order.addPizza(sp2)

    assert order.getOrderDescription() == \
"******\n\
Order Time: 240001\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ double cheese\n\
\t+ tomatoes\n\
Price: $9.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Cheesey\n\
Price: $12.00\n\
\n\
----\n\
CUSTOM PIZZA\n\
Size: L\n\
Toppings:\n\
\t+ chicken\n\
\t+ onions\n\
Price: $14.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: M\n\
Name: The UFO\n\
Price: $14.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $49.00\n\
******\n"   

def test_OrderQueue():
    a = OrderQueue()
    cp1 = CustomPizza("S")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    sp1 = SpecialtyPizza("S", "Carne-more")
    order1 = PizzaOrder(123000)
    order1.addPizza(cp1)
    order1.addPizza(sp1)
    order2 = PizzaOrder(131423)
    order2.addPizza(cp1)
    order3 = PizzaOrder(225659)
    order3.addPizza(sp1)
    a.addOrder(order3)
    a.addOrder(order2)
    a.addOrder(order1)
    assert a.OrderList[1].getTime() == 123000
    assert a.processNextOrder() == "******\n\
Order Time: 123000\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $9.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $21.00\n\
******\n"
    assert a.OrderList[1].time == 131423
    order4 = PizzaOrder(100000)
    order4.addPizza(sp1)
    a.addOrder(order4)
    assert a.OrderList[1].getTime() == 100000