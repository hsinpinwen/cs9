class Car:
    def __init__(self, make, model, year, price):
        self.make = make.upper()
        self.model = model.upper()
        self.year = year
        self.price = price
    
    def __gt__(self, rhs):
        if self.make > rhs.make:
            return True
        elif self.make == rhs.make:
            if self.model > rhs.model:
                return True
            elif self.model == rhs.model:
                if self.year > rhs.year:
                    return True
                elif self.year == rhs.year:
                    if self.price > rhs.price:
                        return True
        else:
            return False
                
    def __lt__(self, rhs):
        if self.make < rhs.make:
            return True
        elif self.make == rhs.make:
            if self.model < rhs.model:
                return True
            elif self.model == rhs.model:
                if self.year < rhs.year:
                    return True
                elif self.year == rhs.year:
                    if self.price < rhs.price:
                        return True
        else:
            return False

    def __eq__(self, rhs):
        if self.make == rhs.make:
            if self.model == rhs.model:
                if self.year == rhs.year:
                    if self.price == rhs.price:
                        return True
        else:
            return False

    def __str__(self):
        return f'Make: {self.make}, Model: {self.model}, Year: {self.year}, Price: ${self.price}'
        #  __  __
        # /  \/  \
        # \      /
        #  \    /
        #   \  /
        #    \/
# c = Car("Honda", "CRV", 2007, 8000)
# print(c)

# c = Car("Honda", "CRV", 2007, 8000)
# c2 = Car("dodge", "DaRt", 2003, 5000)
# print(c > c2)