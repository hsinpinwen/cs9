from Beverage import Beverage
from Coffee import Coffee
from FruitJuice import FruitJuice
from DrinkOrder import DrinkOrder

def test_Beverage():
    b = Beverage(50, 12.4)
    assert b.getOunces() == 50
    assert b.getPrice() == 12.4
    assert b.getInfo() == "50 oz, $12.40"
    b.updateOunces(100)
    b.updatePrice(3.14)
    assert b.getOunces() == 100
    assert b.getPrice() == 3.14
    assert b.getInfo() == "100 oz, $3.14"
    b.updateOunces(1)
    b.updatePrice(0)
    assert b.getOunces() == 1
    assert b.getPrice() == 0
    assert b.getInfo() == "1 oz, $0.00"

def test_Coffee():
    c = Coffee(16, 5, 'Mocha')
    assert c.getInfo() == "Mocha Coffee, 16 oz, $5.00"

def test_FruitJuice():
    fj = FruitJuice(40, 8.64, ['Banana', 'Raspberry', 'Pineapple'])
    assert fj.getInfo() == "Banana/Raspberry/Pineapple Juice, 40 oz, $8.64"

def test_DrinkOrder():
    c = Coffee(18, 9, "Macchiato")
    fj = FruitJuice(69, 4.20, ['Lychee', 'Dragonfruit', 'Starfruit', 'Mango'])
    total_order = DrinkOrder()
    total_order.addBeverage(c)
    total_order.addBeverage(fj)
    assert total_order.getTotalOrder() == "Order Items:\n* Macchiato Coffee, 18 oz, $9.00\n* Lychee/Dragonfruit/Starfruit/Mango Juice, 69 oz, $4.20\nTotal Price: $13.20"
