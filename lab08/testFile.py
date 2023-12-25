from Car import Car
# from CarInventoryNode import CarInventoryNode
from CarInventory import CarInventory

def test_Car_str():
    c = Car("Honda", "CRV", 2007, 8000)
    assert str(c) == "Make: HONDA, Model: CRV, Year: 2007, Price: $8000"
    c2 = Car("mAzDa", "5", 2015, 10000)
    assert str(c2) == "Make: MAZDA, Model: 5, Year: 2015, Price: $10000"

def test_InOrder_ex():
    bst = CarInventory()
    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)
    assert bst.inOrder() == ""
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    assert bst.inOrder() == \
"""\
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""

def test_inOrder():
    bst = CarInventory()
    car1 = Car("GMC", "Yukon", 1996, 7000)
    car2 = Car("GMC", "Yukon", 2023, 40000)
    car3 = Car("Dodge", "Durango", 2023, 50000)
    car4 = Car("Bugatti", "Veyron", 2011, 2000000)
    car5 = Car("Porche", "911", 2023, 120000)
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    assert bst.inOrder() == \
"""\
Make: BUGATTI, Model: VEYRON, Year: 2011, Price: $2000000
Make: DODGE, Model: DURANGO, Year: 2023, Price: $50000
Make: GMC, Model: YUKON, Year: 1996, Price: $7000
Make: GMC, Model: YUKON, Year: 2023, Price: $40000
Make: PORCHE, Model: 911, Year: 2023, Price: $120000
"""

def test_preOrder_ex():
    bst = CarInventory()
    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)
    assert bst.inOrder() == ""
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    assert bst.preOrder() == \
"""\
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""

def test_preOrder():
    bst = CarInventory()
    car1 = Car("GMC", "Yukon", 1996, 7000)
    car2 = Car("GMC", "Yukon", 2023, 40000)
    car3 = Car("Dodge", "Durango", 2023, 50000)
    car4 = Car("Bugatti", "Veyron", 2011, 2000000)
    car5 = Car("Porche", "911", 2023, 120000)
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    assert bst.preOrder() == \
"""\
Make: GMC, Model: YUKON, Year: 1996, Price: $7000
Make: GMC, Model: YUKON, Year: 2023, Price: $40000
Make: DODGE, Model: DURANGO, Year: 2023, Price: $50000
Make: BUGATTI, Model: VEYRON, Year: 2011, Price: $2000000
Make: PORCHE, Model: 911, Year: 2023, Price: $120000
"""

def test_postOrder_ex():
    bst = CarInventory()
    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)
    assert bst.inOrder() == ""
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    assert bst.postOrder() == \
"""\
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
"""

def test_postOrder():
    bst = CarInventory()
    car1 = Car("GMC", "Yukon", 1996, 7000)
    car2 = Car("GMC", "Yukon", 2023, 40000)
    car3 = Car("Dodge", "Durango", 2023, 50000)
    car4 = Car("Bugatti", "Veyron", 2011, 2000000)
    car5 = Car("Porche", "911", 2023, 120000)
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    assert bst.postOrder() == \
"""\
Make: BUGATTI, Model: VEYRON, Year: 2011, Price: $2000000
Make: DODGE, Model: DURANGO, Year: 2023, Price: $50000
Make: PORCHE, Model: 911, Year: 2023, Price: $120000
Make: GMC, Model: YUKON, Year: 1996, Price: $7000
Make: GMC, Model: YUKON, Year: 2023, Price: $40000
"""

def test_doesCarExist():
    bst = CarInventory()
    car1 = Car("GMC", "Yukon", 1996, 7000)
    car2 = Car("GMC", "Yukon", 2023, 40000)
    bst.addCar(car1)
    assert bst.doesCarExist(car1) == True
    assert bst.doesCarExist(car2) == False
    bst.addCar(car2)
    assert bst.doesCarExist(car2) == True

def test_getBestCar_ex():
    bst = CarInventory()
    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    assert bst.getBestCar("Nissan", "Leaf") == car1
    assert bst.getBestCar("Mercedes", "Sprinter") == car3
    assert bst.getBestCar("Honda", "Accord") == None

def test_getBestCar():
    bst = CarInventory()
    car1 = Car("GMC", "Yukon", 1996, 7000)
    car2 = Car("GMC", "Yukon", 2023, 40000)
    car3 = Car("Dodge", "Durango", 2023, 50000)
    car4 = Car("Bugatti", "Veyron", 2011, 2000000)
    car5 = Car("Porche", "911", 2023, 120000)
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    assert bst.getBestCar("GMC", "Yukon") == car2
    assert bst.getBestCar("Bugatti", "Veyron") == car4
    assert bst.getBestCar("Candy", "Crush") == None

def test_getWorstCar_ex():
    bst = CarInventory()
    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    assert bst.getWorstCar("Nissan", "Leaf") == car1
    assert bst.getWorstCar("Mercedes", "Sprinter") == car4
    assert bst.getBestCar("Honda", "Accord") == None

def test_getWorstCar():
    bst = CarInventory()
    car1 = Car("GMC", "Yukon", 1996, 7000)
    car2 = Car("GMC", "Yukon", 2023, 40000)
    car3 = Car("Dodge", "Durango", 2023, 50000)
    car4 = Car("Bugatti", "Veyron", 2011, 2000000)
    car5 = Car("Porche", "911", 2023, 120000)
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    assert bst.getWorstCar("GMC", "Yukon") == car1
    assert bst.getWorstCar("Porche", "911") == car5
    assert bst.getWorstCar("Candy", "Crush") == None

def test_getTotalInventoryPrice_ex():
    bst = CarInventory()
    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    assert bst.getTotalInventoryPrice() == 158000

def test_getTotalInventoryPrice():
    bst = CarInventory()
    car1 = Car("GMC", "Yukon", 1996, 7000)
    car2 = Car("GMC", "Yukon", 2023, 40000)
    car3 = Car("Dodge", "Durango", 2023, 50000)
    car4 = Car("Bugatti", "Veyron", 2011, 2000000)
    car5 = Car("Porche", "911", 2023, 120000)
    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    assert bst.getTotalInventoryPrice() == 2217000