class Animal:
    ''' Animal class type that contains attributes for all animals '''
    def __init__(self, species=None, weight=None, age=None, name=None):
        self.species = species
        if self.species != None:
            self.species = species.upper()
        self.weight = weight
        self.age = age
        self.name = name
        if self.name != None:
            self.name = name.upper()
    
    def setSpecies(self, species):
        self.species = species.upper()

    def setWeight(self, weight):
        self.weight = weight

    def setAge(self, age):
        self.age = age

    def setName(self, name):
        self.name = name.upper()

    def toString(self):
        return("Species: {}, Name: {}, Age: {}, Weight: {}" \
        .format(self.species, self.name, self.age, self.weight))

a = Animal("dog", 8.0, 5, "zorra")
b = Animal("dog", 25.0, 10, "maggie")
c = Animal("dog", 12.2, 1, "cora")
ani_list = [a, b, c]
string = ""
for animal in ani_list[:-1]:
    string = string + animal.toString() + '\n'
string = string + ani_list[-1].toString()
print(string)
