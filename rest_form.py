import tkinter as tk
from tkinter import messagebox
import json
import rest_classes as cl

def read_menu_file():
    with open('menu.json', 'r') as f:
        data = json.load(f)
    return data

def main_menu():
    menu=cl.Menu()
    menu_file = read_menu_file()
    for key,item in menu_file['drink'].items():
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
            #print(name)
            # print(det)

menu = read_menu_file()
main_menu()

window = tk.Tk()
window.title('Yammy restaurant')

mainFrame = tk.Frame(window)
mainFrame.pack(padx=10,pady=10)
welcomeFrame = tk.Frame(mainFrame)
welcomeFrame.grid(row=0,column=0)
welcomeText = tk.Label(welcomeFrame, font=("Arial",20), text="Welcome to Yammy Restaurant!")
welcomeText.pack()

itemsFrame = tk.LabelFrame(mainFrame, text="Yammy menu")
itemsFrame.grid(row=1,column=0)

col=0
photo=[]
for key,item in menu['drink'].items():
    #print(key)
    #print(item['img'])
    photo.append(tk.PhotoImage(file=item['img']))
    testText = tk.Label(itemsFrame, image=photo[col], text=key, compound="top")
    testText.grid(row=0,column=col)
    col += 1

window.mainloop()
