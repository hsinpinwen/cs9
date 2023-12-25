from Apartment import Apartment

def mergesort(apartmentList):
    if len(apartmentList)>1:
        mid = len(apartmentList)//2
        lefthalf = apartmentList[:mid]
        righthalf = apartmentList[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j] or lefthalf[i] == righthalf[j]:
                apartmentList[k]=lefthalf[i]
                i=i+1
            else:
                apartmentList[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            apartmentList[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            apartmentList[k]=righthalf[j]
            j=j+1
            k=k+1

def ensureSortedAscending(apartmentList):
    for i in range(len(apartmentList)-1):
        if apartmentList[i] > apartmentList[i+1]:
            return False
        else:
            return True

def getBestApartment(apartmentList):
    mergesort(apartmentList)
    return apartmentList[0].getApartmentDetails()

def getWorstApartment(apartmentList):
    mergesort(apartmentList)
    return apartmentList[-1].getApartmentDetails()

def getAffordableApartments(apartmentList, budget):
    affordablelist = []
    affordable = ""
    mergesort(apartmentList)
    for apartment in apartmentList:
        if apartment.getRent() <= budget:
            affordablelist.append(apartment.getApartmentDetails())
            affordable = "\n".join(affordablelist)
    return affordable

# a0 = Apartment(1200, 200, "average")
# a1 = Apartment(1200, 200, "excellent")
# a2 = Apartment(1000, 100, "average")
# a3 = Apartment(1000, 215, "excellent")
# a4 = Apartment(700, 315, "bad")
# a5 = Apartment(800, 250, "excellent")
# apartmentList = [a0, a1, a2, a3, a4, a5]

# a1=Apartment(100,200,"excellent")
# a2=Apartment(150,250,"bad")
# a3=Apartment(120,50,"average")
# a4=Apartment(120,50,"average")
# a5=Apartment(120,50,"excellent")
# apartmentList = [a1, a2, a3, a4, a5]

# assert ensureSortedAscending(apartmentList) == False

# print('Best Apartment in apartmentList:')
# print(getBestApartment(apartmentList))

# print('Worst Apartment in apartmentList:')
# print(getWorstApartment(apartmentList))