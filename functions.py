import json
import rest_classes as cl
from tkinter import messagebox
def read_menu_file():
    try:
        with open('menu.json', 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        messagebox.showerror("Error", "File 'menu.json' is not found.")

def main_menu():
    main_menu=[]
    menu_file = read_menu_file()
    drinks(menu_file, main_menu)
    food(menu_file, main_menu)
    return main_menu

def drinks(menu_file, main_menu):
    for key,item in menu_file['drink'].items():
        menu=cl.Menu(key, item['img'])
        drink_type=key
        for name,det in item['items'].items():
            if drink_type=="hot drink":
                if 'options' in det.keys():
                    options=det['options']
                else:
                    options={}
                drink=cl.HotDrink(name, det['price'], det['cals'], options)
            else:
                drink=cl.ColdDrink(name, det['price'], det['cals'])
            menu.items.append(drink)
        main_menu.append(menu)

def get_food(food):
    foods={"soup": cl.Soup, "salad": cl.Salad, "sandwich": cl.Sandwich}
    return foods[food]
def food(menu_file, main_menu):
    for key,item in menu_file['food'].items():
        menu=cl.Menu(key, item['img'])
        for name, det in item['items'].items():
            food=get_food(key)(name, det['price'], det['cals'], det['description'])
            menu.items.append(food)
        main_menu.append(menu)
