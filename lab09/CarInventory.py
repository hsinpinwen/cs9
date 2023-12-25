from Car import Car
from CarInventoryNode import CarInventoryNode

class CarInventory:
    def __init__(self):
        self.root = None
        self.size = 0

    def addCar(self, car):
        if self.root != None:
            self._addCar(car, self.root)
        else:
            self.root = CarInventoryNode(car)

    def _addCar(self, car, cur_node):
        if car.make == cur_node.getMake() and car.model == cur_node.getModel():
            cur_node.cars.append(car)
        elif car < cur_node:
            if cur_node.getLeft() == None:
                new_node = CarInventoryNode(car)
                cur_node.setLeft(new_node)
                new_node.setParent(cur_node)
            else:
                self._addCar(car, cur_node.left)
        else:
            if cur_node.getRight() == None:
                new_node = CarInventoryNode(car)
                cur_node.setRight(new_node)
                new_node.setParent(cur_node)
            else:
                self._addCar(car, cur_node.right)

    def doesCarExist(self, car):
        if self.root == None:
            return False
        if self.root != None:
            return self._doesCarExist(car, self.root)
        
    def _doesCarExist(self, car, cur_node):
        if car.make == cur_node.getMake() and car.model == cur_node.getModel():
            for i in cur_node.cars:
                if car == i:
                    return True
            return False
        elif car < cur_node:
            if cur_node.getLeft() is not None:
                return self._doesCarExist(car, cur_node.getLeft())
            else:
                return False
        else:
            if cur_node.getRight() is not None:
                return self._doesCarExist(car, cur_node.getRight())
            else:
                return False

    def inOrder(self):
        return self._inOrder(self.root)

    def _inOrder(self, cur_node):
        ret = ""
        if cur_node != None:
            ret += self._inOrder(cur_node.left)
            for car in cur_node.cars:
                ret += str(car) + "\n"
            ret += self._inOrder(cur_node.right)
        return ret

    def preOrder(self):
        return self._preOrder(self.root)
    
    def _preOrder(self, cur_node):
        ret = ""
        if cur_node != None:
            for car in cur_node.cars:
                ret += str(car) + "\n"
            ret += self._preOrder(cur_node.left)
            ret += self._preOrder(cur_node.right)
        return ret

    def postOrder(self):
        return self._postOrder(self.root)
    
    def _postOrder(self, cur_node):
        ret = ""
        if cur_node != None:
            ret += self._postOrder(cur_node.left)
            ret += self._postOrder(cur_node.right)
            for car in cur_node.cars:
                ret += str(car) + "\n"
        return ret
    
    def getBestCar(self, make, model):
        if self.root == None:
            return None
        else:
            return self._getBestCar(make.upper(), model.upper(), self.root)
        
    def _getBestCar(self, make, model, cur_node):
        if cur_node.getMake() == make and cur_node.getModel() == model:
            best_car = cur_node.cars[0]
            for i in cur_node.cars:
                if i > best_car:
                    best_car = i
            return best_car
        elif cur_node.getMake() > make or (cur_node.getMake() == make and cur_node.getModel() > model):
            if cur_node.getLeft() != None:
                return self._getBestCar(make, model, cur_node.getLeft())
        else:
            if cur_node.getRight() != None:
                return self._getBestCar(make, model, cur_node.getRight())
            
    def getWorstCar(self, make, model):
        if self.root == None:
            return None
        else:
            return self._getWorstCar(make.upper(), model.upper(), self.root)
        
    def _getWorstCar(self, make, model, cur_node):
        if cur_node.getMake() == make and cur_node.getModel() == model:
            worst_car = cur_node.cars[0]
            for i in cur_node.cars:
                if i < worst_car:
                    worst_car = i
            return worst_car
        elif cur_node.getMake() > make or (cur_node.getMake() == make and cur_node.getModel() > model):
            if cur_node.getLeft() != None:
                return self._getWorstCar(make, model, cur_node.getLeft())
        else:
            if cur_node.getRight() != None:
                return self._getWorstCar(make, model, cur_node.getRight())
            
    def getTotalInventoryPrice(self):
        if self.root != None:
            return self._getTotalInventoryPrice(self.root)
        else:
            return 0
        
    def _getTotalInventoryPrice(self, cur_node):
        total_price = 0
        for car in cur_node.cars:
            total_price += car.price
        if cur_node.getLeft() != None:
            total_price += self._getTotalInventoryPrice(cur_node.getLeft())
        if cur_node.getRight() != None:
            total_price += self._getTotalInventoryPrice(cur_node.getRight())
        return total_price
    
    def getSuccessor(self, make, model):
        if self.root == None:
            return None
        else:
            cur_node = self.findNode(make.upper(), model.upper(), self.root)
            if cur_node is None:
                return None
            successor = self.findSuccessor(cur_node)
            return successor

    def findNode(self, make, model, cur_node):
        if cur_node is None:
            return None
        if cur_node.getMake() == make and cur_node.getModel() == model:
            return cur_node
        elif cur_node.getMake() > make or (cur_node.getMake() == make and cur_node.getModel() > model):
            return self.findNode(make, model, cur_node.getLeft())
        else:
            return self.findNode(make, model, cur_node.getRight())

    def findSuccessor(self, cur_node):
        if cur_node.getRight() != None:
            return self.findMin(cur_node.getRight())
        else:
            current = cur_node
            parent = current.getParent()
            while parent != None and current == parent.getRight():
                current = parent
                parent = current.getParent()
            return parent

    def findMin(self, cur_node):
        current = cur_node
        while current.getLeft() is not None:
            current = current.getLeft()
        return current

    def removeCar(self, make, model, year, price):
        if self.root is None:
            return False
        else:
            cur_node = self.findNode(make.upper(), model.upper(), self.root)
            if cur_node is None:
                return False
            for car in cur_node.cars:
                if car.make == make.upper() and car.model == model.upper() and car.year == year and car.price == price:
                    cur_node.cars.remove(car)
                    self.size -= 1
                    if len(cur_node.cars) == 0:
                        self.removeCarNode(cur_node)
                    return True
            return False

    # def removeCar(self, make, model, year, price):
    #     if self.root is None:
    #         return False
    #     else:
    #         return self._removeCar(make.upper(), model.upper(), year, price, self.root)

    def _removeCar(self, make, model, year, price, cur_node):
        if cur_node is None:
            return False

        for car in cur_node.cars:
            if car.make == make and car.model == model and car.year == year and car.price == price:
                cur_node.cars.remove(car) 

                if len(cur_node.cars) == 0:
                    self.removeCarNode(cur_node) 
                    
                return True

        if make < cur_node.getMake() or (make == cur_node.getMake() and model < cur_node.getModel()):
            return self._removeCar(make, model, year, price, cur_node.getLeft())
        else:
            return self._removeCar(make, model, year, price, cur_node.getRight())

    def removeCarNode(self, cur_node):
        parent = cur_node.getParent()

        if cur_node.getLeft() is None and cur_node.getRight() is None:
            if parent is None:
                self.root = None  
            elif parent.getLeft() == cur_node:
                parent.setLeft(None)  
            else:
                parent.setRight(None)  

        elif cur_node.getLeft() is None:
            if parent is None:
                self.root = cur_node.getRight()  
            elif parent.getLeft() == cur_node:
                parent.setLeft(cur_node.getRight()) 
            else:
                parent.setRight(cur_node.getRight())  

            cur_node.getRight().setParent(parent)  

        elif cur_node.getRight() is None:
            if parent is None:
                self.root = cur_node.getLeft() 
            elif parent.getLeft() == cur_node:
                parent.setLeft(cur_node.getLeft())  
            else:
                parent.setRight(cur_node.getLeft()) 

            cur_node.getLeft().setParent(parent)  
        else:
            successor = self.findSuccessor(cur_node) 
            cur_node.cars = successor.cars 

            self.removeCarNode(successor)

        return True
    
# bst = CarInventory()
# car1 = Car("Mazda", "CX-5", 2022, 25000)
# car2 = Car("Tesla", "Model3", 2018, 50000)
# car3 = Car("BMW", "X5", 2022, 60000)
# car4 = Car("BMW", "X5", 2020, 58000)
# car5 = Car("Audi", "A3", 2021, 25000)
# bst.addCar(car1)
# bst.addCar(car2)
# bst.addCar(car3)
# bst.addCar(car4)
# bst.addCar(car5)
# print(bst.getSuccessor("Audi", "A3"))

# print(bst.getWorstCar("Mercedes", "Sprinter"))
# assert bst.inOrder() == \
# """\
# Make: FORD, Model: RANGER, Year: 2021, Price: $25000
# Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
# Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
# Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
# Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
# """

# bst.removeCar("BMW", "X5", 2020, 58000)

#                                  Mazda,CX-5,[Car(Mazda,CX-5,2022,25000)]
#                                 /                                       \
#           BMW,X5,[Car(BMW,X5,2022,60000)]    Tesla,Model3,[Car(Tesla,Model3,2018,50000)]
#                   /
#  Audi,A3,[Car(Audi,A3,2021,25000)]

# print(bst.inOrder())
# """\
# Make: AUDI, Model: A3, Year: 2021, Price: $25000
# Make: BMW, Model: X5, Year: 2022, Price: $60000
# Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
# Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
# """

# print(bst.inOrder())

# assert bst.preOrder() == \
# """\
# Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
# Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
# Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
# Make: FORD, Model: RANGER, Year: 2021, Price: $25000
# Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
# """
# print(bst.preOrder())

# assert bst.postOrder() == \
# """\
# Make: FORD, Model: RANGER, Year: 2021, Price: $25000
# Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
# Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
# Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
# Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
# """
# print(bst.postOrder())

# bst = CarInventory()
# car1 = Car("GMC", "Yukon", 1996, 7000)
# car2 = Car("GMC", "Yukon", 2023, 40000)
# car3 = Car("Dodge", "Durango", 2023, 50000)
# car4 = Car("Bugatti", "Veyron", 2011, 2000000)
# car5 = Car("Porche", "911", 2023, 120000)
# bst.addCar(car1)
# bst.addCar(car2)
# bst.addCar(car3)
# bst.addCar(car4)
# bst.addCar(car5)

# print(bst.inOrder())
# print(bst.preOrder())
# print(bst.postOrder())
# print(bst.getTotalInventoryPrice())
