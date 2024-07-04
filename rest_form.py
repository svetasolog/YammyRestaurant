import tkinter as tk
from tkinter import messagebox

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
testText = tk.Label(itemsFrame, text="TEST Yammy item")
testText.grid(row=0,column=0)

window.mainloop()