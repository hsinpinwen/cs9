from Car import Car
from CarInventoryNode import CarInventoryNode

class CarInventory:
    def __init__(self):
        self.root = None
        # self.size = 0

    def addCar(self, car):
        if self.root == None:
            self.root = CarInventoryNode(car)
        else:
            self._put(car, self.root)

    def _put(self, car, cur_node):
        if car.make == cur_node.car.make and car.model == cur_node.car.model:
            cur_node.cars.append(car)
        elif car < cur_node.car:
            if cur_node.left == None:
                cur_node.left = CarInventoryNode(car)
            else:
                self._put(car, cur_node.left)
        elif car > cur_node.car:
            if cur_node.right == None:
                cur_node.right = CarInventoryNode(car)
            else:
                self._put(car, cur_node.right)

    def doesCarExist(self, car):
        if self.root:
            res = self._doesCarExist(car, self.root)
            if res:
                for i in res.cars:
                    if car == i:
                        return True
                return False
            else:
                return False
        else:
            return False

    def _doesCarExist(self, car, cur_node):
        if not cur_node:
            return None
        elif cur_node.make == car.make and cur_node.model == car.model:
            return cur_node
        elif car.make < cur_node.make or car.make == cur_node.make and car.model < cur_node.model:
            return self._doesCarExist(car, cur_node.left)
        else:
            return self._doesCarExist(car, cur_node.right)

    def inOrder(self):
        return self._inOrder(self.root)
    
    # def inorder(tree):
    #     ret = ""
    #     if tree != None:
    #         ret += inorder(tree.getLeftChild())
    #         ret += tree.getRootValue()
    #         ret += inorder(tree.getRightChild())
    #     return ret

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

    # def getCar(self, car):
    #     return self._getCar(car, self.root)
    
    # def _getCar(self, car, cur_node):
    #     if car.make == cur_node.make and car.model == cur_node.model:
    #         return cur_node
    #     elif car < cur_node.car:
    #         return self._getCar(car, cur_node.getLeft())
    #     elif car > cur_node.car:
    #         return self._getCar(car, cur_node.getRight())
        
    def getBestCar(self, make, model):
        temp_car = Car(make, model, 0, 0)
        temp_car_node = CarInventoryNode(temp_car)
        match = self._doesCarExist(temp_car_node, self.root)
        if match:
            best_car = match.cars[0]
            for i in match.cars:
                if i > best_car:
                    best_car = i
            return best_car

    def getWorstCar(self, make, model):
        temp_car = Car(make, model, 0, 0)
        temp_car_node = CarInventoryNode(temp_car)
        match = self._doesCarExist(temp_car_node, self.root)
        if match:
            worst_car = match.cars[0]
            for i in match.cars:
                if i < worst_car:
                    worst_car = i
            return worst_car

    def getTotalInventoryPrice(self):
        if self.root != None:
            return self._getTotalInventoryPrice(self.root)
        else:
            return 0
        
    def _getTotalInventoryPrice(self, cur_node):
        total_price = 0
        if cur_node != None:
            for i in cur_node.cars:
                total_price += i.price
            total_price += self._getTotalInventoryPrice(cur_node.getLeft())
            total_price += self._getTotalInventoryPrice(cur_node.getRight())
        return total_price
        
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

# print(bst.getWorstCar("Mercedes", "Sprinter"))
# assert bst.inOrder() == \
# """\
# Make: FORD, Model: RANGER, Year: 2021, Price: $25000
# Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
# Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
# Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
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
