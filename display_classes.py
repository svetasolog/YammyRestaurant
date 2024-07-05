import tkinter as tk

class MenuCard():
    def __init__(self, root, photo, menu, i, row, items):
        self.label = tk.Label(root, image=photo, text=menu, compound="top", cursor="hand2")
        self.label.grid(row=row, column=i, padx=10, pady=10)
        self.label.bind("<Button-1>", self.show_details)
        self.items=items
    def show_details(self, event):
        print(self.items)