import tkinter as tk
from tkinter import ttk
import functions as func
from tkinter import messagebox

class RestApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Yammy Restaurant")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (CategoryFrame, MenuFrame):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("CategoryFrame")
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
    def get_frame(self, page_name):
        return self.frames[page_name]
class CategoryFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        welcomeFrame = tk.Frame(self)
        welcomeFrame.grid(row=0, column=0)
        welcomeText = tk.Label(welcomeFrame, font=("Arial", 20), text="Welcome to Yammy Restaurant!")
        welcomeText.pack(padx=30, pady=15)

        itemsFrame = tk.LabelFrame(self, text="Yammy menu")
        itemsFrame.grid(row=1, column=0, padx=15, pady=15)

        menu = func.main_menu()
        photo = []
        row = 0
        for i in range(len(menu)):
            if i % 3 == 0:
                row += 1
            photo.append(tk.PhotoImage(file=menu[i].img))
            MenuCard(itemsFrame, photo[i], menu[i].name, i, row, menu[i].items, self.controller)

class MenuCard():
    def __init__(self, root, photo, menu, i, row, items, controller):
        self.controller = controller
        self.items = items
        self.label = tk.Label(root, image=photo, text=menu, compound="top", cursor="hand2")
        self.label.grid(row=row, column=i, padx=10, pady=10)
        self.label.bind("<Button-1>", lambda e: self.menu_frame(self.items))
    def menu_frame(self, items):
        self.controller.show_frame("MenuFrame")
        self.controller.get_frame("MenuFrame").show_item(items)

class MenuFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        button = tk.Button(self, text="<< Back to Main Menu",
                           command=lambda: controller.show_frame("CategoryFrame"))
        button.pack(pady=15)
        self.category=tk.StringVar()
        header = tk.Label(self, font=("Arial", 15), textvariable=self.category)
        header.pack()
        self.itemsFrame = tk.LabelFrame(self, text="Yammy menu")
        self.itemsFrame.pack()

    def show_item(self, items):
        self.category.set(items[0].show_category())
        self.itemsFrame.destroy()
        self.itemsFrame = tk.LabelFrame(self, text="Yammy menu")
        self.itemsFrame.pack(padx=20, pady=15)
        for i in range(len(items)):
            ItemLine(self.itemsFrame, items[i], i)

class ItemLine():
    def __init__(self, root, item, i):
        self.name = tk.Label(root,
                             text=item.get_name(),
                             width=30,
                             height=3,
                             font=("Arial", 10, "bold"),
                             background='lightgreen')
        self.name.grid(row=i, column=0, padx=10, pady=5)
        self.price = tk.Label(root, text=f"${item.get_price()}")
        self.price.grid(row=i, column=1, padx=10)
        self.cals = tk.Label(root, text=f"{item.get_cals()} Cals")
        self.cals.grid(row=i, column=2, padx=10)
        self.optsFrame = tk.LabelFrame(root, text="Options")
        self.optsFrame.grid(row=i, column=3, padx=10)
        self.opt=[]
        n=0
        for opt, points in item.get_options().items():
            self.opt.append(Option(self.optsFrame, opt, n, points))
            n+=1
        self.quantity = tk.Spinbox(root, from_=1, to=50, width=3)
        self.quantity.grid(row=i, column=4, padx=10)
        self.addBtn = tk.Button(root, text="Add", width=15, command=self.add_item)
        self.addBtn.grid(row=i, column=5, padx=10)
    def add_item(self):
        try:
            self.opts=""
            for opt in self.opt:
                self.opts+=opt.get_option()+", "

            with open('order.txt', 'a') as fwrite:
                fwrite.write(f"{self.name.cget("text")}, {self.price.cget("text")}, {self.cals.cget("text")}, {self.opts}{self.quantity.get()}, ${self.calc_sum()}\n")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    def calc_sum(self):
        try:
            sum = float(self.price.cget("text").strip("$"))*int(self.quantity.get())
            return sum
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

class Option():
    def __init__(self, root, opt, n, points):
        self.labelName = tk.Label(root, text=opt)
        self.labelName.grid(row=n, column=0)
        self.options = ttk.Combobox(root, values=points, width=20)
        self.options.grid(row=n, column=1, padx=10, pady=2)
        self.options.current(0)
    def get_option(self):
        return f"{self.labelName.cget("text")}:{self.options.get()}"
