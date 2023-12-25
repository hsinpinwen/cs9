from Animal import Animal

class AnimalShelter:
    ''' Class representing a collection of courses. Courses are
    organized by a dictionary where the key of the dictionary will 
    be a str type representing an Animal’s species and the corresponding value is
    a list of Animal objects that the AnimalShelter contains'''
    def __init__(self):
        self.AnimalShelter = {} # empty dictionary

    def addAnimal(self, animal):
        if animal.species in self.AnimalShelter:
            self.AnimalShelter[animal.species].append(animal)
        else:
            self.AnimalShelter[animal.species] = [animal]

    def removeAnimal(self,animal):               
        if animal.species in self.AnimalShelter:            
            if len(self.AnimalShelter[animal.species]) > 0:
                self.AnimalShelter[animal.species].remove(animal)

    def removeSpecies(self, species):
        if species.upper() in self.AnimalShelter:
            del self.AnimalShelter[species.upper()]

    def getAnimalsBySpecies(self, species):
        species = species.upper()
        string = ""
        if species in self.AnimalShelter:
            if len(self.AnimalShelter[species]) == 0:
                return string
            else:
                for animal in self.AnimalShelter[species][:-1]:
                    string = string + animal.toString() + '\n'
                string = string + self.AnimalShelter[species][-1].toString()
            return string
        else:
            return string
        # string = ""
        # for animal in ani_list[:-1]:
        #     string = string + animal.toString() + '\n'
        # string = string + ani_list[-1].toString()
        # print(string)

    def doesAnimalExist(self, animal):
        for item in self.AnimalShelter.keys():
            if animal in self.AnimalShelter[item]:
                return True
        return False