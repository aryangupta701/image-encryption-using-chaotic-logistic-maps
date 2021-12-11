from tkinter import Tk , PhotoImage , Label , Button , Text, messagebox 
import encrypt as en
from tkinter import * 
from tkinter import filedialog

def open_file():
    file = filedialog.askopenfile(mode='r', filetypes=[('BITMAP Files', '*.bmp')])
    if file:
        browselabel.config(text=file.name)


def pass_alert():
    messagebox.showinfo("Key Alert","Please enter a Valid Key.")


def encryption():
    key = entry1.get("1.0",END)
    if(len(key) != 11):
        pass_alert()
        return;
    en.encryption(key , True , browselabel.cget("text"))
    
def decryption():
    key = entry1.get("1.0",END)
    if(len(key) != 11):
        pass_alert()
        return;
    en.encryption(key, False, browselabel.cget("text"))
    
root = Tk()
root.geometry("600x400")
root.title('Image Encryption') 

photo = PhotoImage(file = "images/back.png")
label1 = Label( root , image = photo )
label1.place(x=-10,y=0)

#entry of key 
keytitle = Label(root, text="Enter Key (10 Char) :", bg="light green")
entry1 = Text(root, height=2, width=15)
entry1.place(x=120,y=120)
keytitle.place(x=100,y=300)

#keylogo place 
keylogo = PhotoImage(file="images/logo.png")
label2 = Label (root , image = keylogo)
label2.place(x=140,y=120)
#browse.grid(row=1, column=0)

#browse TEXT 
browselabel = Label(root, text="Select a file please", bg="light green")
browselabel.place(x=23,y=128)

#browsebutton 
browsebutton = Button(root, text ="Browse", 
                      command = open_file)
browsebutton.place(x=300,y=200)

#encrypt Button 
encryptButton = Button(root, text ="Encrypt", 
                      command = encryption)
encryptButton.place(x=100,y=200)

#decrypt Button 
decryptButton = Button(root, text ="Decrypt", 
                      command = decryption)
decryptButton.place(x=200,y=200)



root.mainloop()
