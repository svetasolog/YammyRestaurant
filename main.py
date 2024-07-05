import tkinter as tk
import display_classes as displ_cl
import functions as func

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

menu = func.main_menu()
photo=[]
row=0
for i in range(len(menu)):
    if i%3==0:
        row+=1
    photo.append(tk.PhotoImage(file=menu[i].img))
    menu_card = displ_cl.MenuCard(itemsFrame, photo[i], menu[i].name, i, row, menu[i].items)

window.mainloop()