import tkinter as tk
import functions as func

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

class CategoryFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        welcomeFrame = tk.Frame(self)
        welcomeFrame.grid(row=0, column=0)
        welcomeText = tk.Label(welcomeFrame, font=("Arial", 20), text="Welcome to Yammy Restaurant!")
        welcomeText.pack()

        itemsFrame = tk.LabelFrame(self, text="Yammy menu")
        itemsFrame.grid(row=1, column=0)

        menu = func.main_menu()
        photo = []
        row = 0
        for i in range(len(menu)):
            if i % 3 == 0:
                row += 1
            photo.append(tk.PhotoImage(file=menu[i].img))
            menu_card = MenuCard(itemsFrame, photo[i], menu[i].name, i, row, menu[i].items, self.controller)

class MenuFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1")
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("CategoryFrame"))
        button.pack()
class MenuCard():
    def __init__(self, root, photo, menu, i, row, items, controller):
        self.controller = controller
        self.label = tk.Label(root, image=photo, text=menu, compound="top", cursor="hand2")
        self.label.grid(row=row, column=i, padx=10, pady=10)
        self.label.bind("<Button-1>", lambda e: self.controller.show_frame("MenuFrame"))
        self.items=items
