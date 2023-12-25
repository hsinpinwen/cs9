# from Car import Car

class CarInventoryNode():
    def __init__(self, car):
        self.car = car
        self.make = car.make
        self.model = car.model
        self.cars = [car]
        self.parent = None
        self.left = None
        self.right = None

    def getMake(self):
        return self.car.make
    
    def getModel(self):
        return self.car.model
    
    def getParent(self):
        return self.parent
    
    def setParent(self, parent):
        self.parent = parent

    def getLeft(self):
        return self.left
    
    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right
    
    def setRight(self, right):
        self.right = right

    def __str__(self):
        cars = []
        for car in self.cars:
            cars.append(str(car))
            cars.append('\n')
        return "".join(cars)

# car1 = Car("Dodge", "dart", 2015, 6000)
# car2 = Car("dodge", "DaRt", 2003, 5000)
# carNode = CarInventoryNode(car1)
# carNode.cars.append(car2)
# print(carNode)
    def hasLeftChild(self):
        return self.left

    def hasRightChild(self):
        return self.right
    
    def isLeftChild(self):
        # if self.parent:
        #     if self.parent.left:
        #         if self.parent.left == self:
        #             return True
        # return False
        return self.parent and self.parent.left == self

    def isRightChild(self):
        # if self.parent:
        #     if self.parent.right:
        #         if self.parent.right == self:
        #             return True
        # return False
        return self.parent and self.parent.right == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.right or self.left)

    def hasAnyChildren(self):
        return self.right or self.left

    def hasBothChildren(self):
        return self.right and self.left