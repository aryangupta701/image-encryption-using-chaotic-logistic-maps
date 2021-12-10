from tkinter import *
from tkinter import filedialog
import encrypt 
root = Tk()

# root.geometry("400*400")
entry1 = Text(root, height=2, width=10)
entry1.place(x=50, y=50)
b1 = Button(root, text="Encrypt", command=encrypt.encryption())
b1.place(x=70, y=10)

        #key = entry1.get(1.0,END)
root.mainloop()