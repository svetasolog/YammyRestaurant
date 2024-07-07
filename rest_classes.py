class Menu():
    def __init__(self, name, img):
        self.name=name
        self.img=img
        self.items=[]

class Item():
    def __init__(self, name, price, cals):
        self.name=name
        self.price=price
        self.cals=cals
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price
    def get_cals(self):
        return self.cals

class Drink(Item):
    def __init__(self, name, price, cals):
        super().__init__(name, price, cals)
    def get_descr(self):
        return ""

class ColdDrink(Drink):
    def __init__(self, name, price, cals):
        super().__init__(name, price, cals)
        self.options = {"Ice":['no ice','ice','light ice','extra ice']}
    def show_category(self):
        return "Cold Drink"
    def get_options(self):
        return self.options

class HotDrink(Drink):
    def __init__(self, name, price, cals, options):
        super().__init__(name, price, cals)
        self.options = options
    def show_category(self):
        return "Hot Drink"
    def get_options(self):
        return self.options


class Food(Item):
    def __init__(self, name, price, cals, descr):
        super().__init__(name, price, cals)
        self.descr = descr
    def get_descr(self):
        return self.descr
class Soup(Food):
    def __init__(self, name, price, cals, descr):
        super().__init__(name, price, cals, descr)
        self.bread = {"Bread": ["no bread", "gluten-free bread", "slice of bread"]}
    def show_category(self):
        return "Soup"
    def get_options(self):
        return self.bread

class Salad(Food):
    def __init__(self, name, price, cals, descr):
        super().__init__(name, price, cals, descr)
        self.dressing = {"Dressing": ["honey balsamic", "house italian"]}
    def show_category(self):
        return "Salad"
    def get_options(self):
        return self.dressing

class Sandwich(Food):
    def __init__(self, name, price, cals, descr):
        super().__init__(name, price, cals, descr)
        self.prep = {"Preparation choice": ["toasted", "not toasted"]}
    def show_category(self):
        return "Sandwich"
    def get_options(self):
        return self.prep
