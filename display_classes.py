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
        for F in (CategoryFrame, MenuFrame, OrderFrame):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("CategoryFrame")
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.fill_out()
        frame.tkraise()
    def get_frame(self, page_name):
        return self.frames[page_name]
class CategoryFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.container = tk.LabelFrame(self, borderwidth=0)
        self.container.pack()
        self.welcomeText = tk.Label(self.container, font=("Arial", 20), text="Welcome to Yammy Restaurant!")
        self.welcomeText.grid(row=0, column=0, padx=30, pady=15)

        self.orderBtn = tk.Button(self.container, text="My Order", width=20, background="white",
                           command=lambda: self.controller.show_frame("OrderFrame"))
        self.orderBtn.grid(row=1, column=0)

        self.itemsFrame = tk.LabelFrame(self.container, text="Yammy menu")
        self.itemsFrame.grid(row=2, column=0, padx=15, pady=15)

        menu = func.main_menu()
        self.photo = []
        row = 0
        col = 0
        for i in range(len(menu)):
            if i % 3 == 0:
                row += 1
                col = 0
            else:
                col += 1
            self.photo.append(tk.PhotoImage(file=menu[i].img))
            MenuCard(self.itemsFrame, self.photo[i], menu[i].name, col, row, menu[i].items, self.controller)

    def fill_out(self):
        return

class MenuCard():
    def __init__(self, root, photo, menu, col, row, items, controller):
        self.root = root
        self.photo = photo
        self.menu = menu
        self.col = col
        self.row = row
        self.controller = controller
        self.items = items
        self.label = tk.Label(self.root, image=self.photo, text=self.menu, compound="top", cursor="hand2", font=("Arial", 12))
        self.label.grid(row=self.row, column=self.col, padx=10, pady=10)
        self.label.bind("<Button-1>", lambda e: self.menu_frame())
    def menu_frame(self):
        self.controller.show_frame("MenuFrame")
        self.controller.get_frame("MenuFrame").show_item(self.items)

class MenuFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.btns = tk.Frame(self)
        self.btns.pack()
        self.menuBtn = tk.Button(self.btns, text="<< Back to Main Menu", width=20, background="white",
                           command=lambda: self.controller.show_frame("CategoryFrame"))
        self.menuBtn.grid(row=0, column=0, pady=15)
        self.orderBtn = tk.Button(self.btns, text="My Order", width=20, background="white",
                           command=lambda: self.controller.show_frame("OrderFrame"))
        self.orderBtn.grid(row=0, column=1, padx=15)

        self.category=tk.StringVar()
        self.header = tk.Label(self, font=("Arial", 15, "bold"), textvariable=self.category)
        self.header.pack()
        self.itemsFrame = tk.LabelFrame(self, text="Yammy menu")
        self.itemsFrame.pack()

    def show_item(self, items):
        self.category.set(items[0].show_category())
        self.itemsFrame.destroy()
        self.itemsFrame = tk.LabelFrame(self, text="Yammy menu")
        self.itemsFrame.pack(padx=20, pady=15)
        for i in range(len(items)):
            ItemLine(self.itemsFrame, items[i], i)
    def fill_out(self):
        return

class ItemLine():
    def __init__(self, root, item, row):
        self.root = root
        self.item = item
        self.row = row
        self.itemFrame = tk.LabelFrame(self.root)
        self.itemFrame.grid(row=self.row, column=0, padx=20, pady=5, sticky="nsew")
        self.name = tk.Label(self.itemFrame,
                             text=self.item.get_name(),
                             width=30,
                             height=3,
                             font=("Arial", 10, "bold"),
                             background="lightgreen")
        self.name.grid(row=0, column=0, padx=10, pady=5)
        self.price = tk.Label(self.itemFrame, width=10, text=f"${self.item.get_price()}", font=("Arial", 10))
        self.price.grid(row=0, column=1, padx=5)
        self.cals = tk.Label(self.itemFrame, width=10, text=f"{self.item.get_cals()} Cals")
        self.cals.grid(row=0, column=2, padx=5)
        self.optsFrame = tk.LabelFrame(self.itemFrame, width=30, text="Options")
        self.optsFrame.grid(row=0, column=3, padx=10, pady=4)
        self.opt=[]
        n = 0
        for opt, points in self.item.get_options().items():
            self.opt.append(Option(self.optsFrame, opt, n, points))
            n += 1
        self.qtyLabel = tk.LabelFrame(self.itemFrame, width=10, text="Qty")
        self.qtyLabel.grid(row=0, column=4)
        self.quantity = tk.Spinbox(self.qtyLabel, from_=1, to=50, width=3)
        self.quantity.grid(row=0, column=0, padx=10, pady=4)
        self.addBtn = tk.Button(self.itemFrame, text="Add", width=15, background="white", command=self.add_item)
        self.addBtn.grid(row=0, column=5, padx=10)
        if self.item.get_descr() != "":
            self.descr = tk.Label(self.itemFrame, text=self.item.get_descr(), width=135)
            self.descr.grid(row=1, columnspan=6, padx=10, sticky="ew")

    def validate(self, user_inp):
        if user_inp=="" or user_inp=="0":
            messagebox.showwarning("Error. Invalid data.", "You must enter the quantity")
        elif not user_inp.isnumeric():
            messagebox.showwarning("Error. Invalid data.", "The quantity must be a number!")
        else:
            return 1
    def add_item(self):
        try:
            self.opts=""
            for opt in self.opt:
                self.opts+=opt.get_option()+"|"

            if self.validate(self.quantity.get()) == 1:
                with open('order.txt', 'a') as fwrite:
                    fwrite.write(f"{self.name.cget("text")}, {self.price.cget("text")}, {self.cals.cget("text")}, {self.opts}, {self.quantity.get()}, ${self.calc_sum()}\n")
                    messagebox.showinfo("Success","The item is added!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    def calc_sum(self):
        try:
            sum = float(self.price.cget("text").strip("$"))*int(self.quantity.get())
            return sum
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

class Option():
    def __init__(self, root, opt, row, points):
        self.root = root
        self.opt = opt
        self.row = row
        self.points = points
        self.labelName = tk.Label(self.root, text=self.opt, width=15)
        self.labelName.grid(row=self.row, column=0)
        self.options = ttk.Combobox(self.root, values=self.points, width=20, state="readonly")
        self.options.grid(row=self.row, column=1, padx=10, pady=5)
        self.options.current(0)
    def get_option(self):
        return f"{self.labelName.cget("text")}: {self.options.get()}"

class OrderFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.menuBtn = tk.Button(self, text="Main Menu", width=20, background="white",
                           command=lambda: self.controller.show_frame("CategoryFrame"))
        self.menuBtn.pack(pady=15)
        header=tk.Label(self, text="My Order", font=("Arial", 15, "bold"))
        header.pack()
        self.itemsFrame = tk.LabelFrame(self, text="Yammy order")
        self.itemsFrame.pack(padx=20, pady=15)

    def fill_out(self):
        self.itemsFrame.destroy()
        self.itemsFrame = tk.LabelFrame(self, text="Yammy order")
        self.itemsFrame.pack(padx=20, pady=15)
        try:
            with open('order.txt', 'r') as self.f:
                i = 0
                sum = 0
                for line in self.f:
                    item = line.strip('\n').split(',')
                    self.one_line(item, i)
                    sum += float(item[5].strip().strip("$"))
                    i += 1
                total = tk.Label(self.itemsFrame, font=("Arial", 12, "bold"), text=f"Total: ${sum}")
                total.grid(row=i+1, column=5, padx=15, pady=3)
        except FileNotFoundError:
            self.noOrder = tk.Label(self.itemsFrame, font=("Arial", 15), text="Please add items from the menu first.")
            self.noOrder.pack()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    def one_line(self, item, row):
        orderName = tk.Label(self.itemsFrame,
                             text=item[0],
                             width=30,
                             height=3,
                             font=("Arial", 10, "bold"),
                             background="lightgreen")
        orderName.grid(row=row, column=0, padx=15, pady=3)
        orderCals = tk.Label(self.itemsFrame, text=item[2])
        orderCals.grid(row=row, column=1, padx=5, pady=3)
        opts = item[3].strip().strip("|").split("|")
        orderOpt = tk.LabelFrame(self.itemsFrame, text="Options")
        orderOpt.grid(row=row, column=2, padx=5, pady=3)
        for r in range(len(opts)):
            opt = tk.Label(orderOpt, text=opts[r], width=20)
            opt.grid(row=r, column=0, padx=5, pady=2)
        orderQuantity = tk.Label(self.itemsFrame, text=f"{item[4]}x")
        orderQuantity.grid(row=row, column=3, padx=5, pady=3)
        orderPrice = tk.Label(self.itemsFrame, text=item[1])
        orderPrice.grid(row=row, column=4, padx=5, pady=3)
        orderSum = tk.Label(self.itemsFrame, text=item[5])
        orderSum.grid(row=row, column=5, padx=5, pady=3)
