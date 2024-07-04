class Menu():
    def __init__(self):
        self.name={}
        self.items=[]
class Item():
    def __init__(self, name, price, cals):
        self.name=name
        self.price=price
        self.cals=cals
    def get_name(self):
        return self.name

class Drink(Item):
    def __init__(self, name, price, cals):
        super().__init__(name, price, cals)

class ColdDrink(Drink):
    def __init__(self, name, price, cals, options=[]):
        super().__init__(name, price, cals)
        self.options = options
        print(f"{self.name}, {self.price}, {self.cals}, {self.options}")
class HotDrink(Drink):
    def __init__(self, name, price, cals, options):
        super().__init__(name, price, cals)
        self.options = options
        print(f"{self.name}, {self.price}, {self.cals}, {self.options}")

class Food(Item):
    def __init__(self, name, price, cals, descr):
        super().__init__(name, price, cals)
        self.descr = descr

class Soup(Food):
    def __init__(self, name, price, cals, descr, bread):
        super().__init__(name, price, cals, descr)
        self.bread = bread

class Salad(Food):
    def __init__(self, name, price, cals, descr, dressing):
        super().__init__(name, price, cals, descr)
        self.dressing = dressing

class Sandwich(Food):
    def __init__(self, name, price, cals, descr, prep):
        super().__init__(name, price, cals, descr)
        self.prep = prep
