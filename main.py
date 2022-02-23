from tkinter import Tk , PhotoImage , Label , Button , Text, messagebox ,Entry
import encrypt as en
from tkinter import * 
from tkinter import filedialog

def open_file():
    file = filedialog.askopenfile(mode='r', filetypes=[('BITMAP Files', '*.bmp')])
    if file:
        browselabel.config(text=file.name)


def pass_alert():
    messagebox.showinfo("Key Alert","Please enter a Valid Key.")

def pass_alert_selectfile_encrypt():
    messagebox.showinfo("File Select Alert","Please enter a File to Encrypt.")
    
def pass_alert_selectfile_decrypt():
    messagebox.showinfo("File Select Alert","Please enter a File to Decrypt.")

def encryption():
    key = entry1.get()
    if(len(key) != 10):
        pass_alert()
        return
    if(browselabel.cget("text") == "Select a file please"):
        pass_alert_selectfile_encrypt()
        return 
    en.encryption(key , True , browselabel.cget("text"))
    
def decryption():
    key = entry1.get()
    if(len(key) != 10):
        pass_alert()
        return
    if(browselabel.cget("text") == "Select a file please"):
        pass_alert_selectfile_decrypt()
        return 
    en.encryption(key, False, browselabel.cget("text"))
    
root = Tk()
root.geometry("600x400+420+200")
root.title('Image Encryption') 

#background image
photo = PhotoImage(file = "images/back.png")
bg = Label( root , image = photo )

#entry of key 
keytitle = Label(root, text="Enter Key : ", 
                 bg="sky blue",font = 10, width=13)
entry1 = Entry(root, width = 14, font = 20,show="*")

#keylogo place 
keylogo = PhotoImage(file="images/logo.png")
keylabel = Label (root , image = keylogo)

#browse TEXT 
browselabel = Label(root, text="Select a file please", 
                    height=2, width=47)

#browse logo 
browselogo = PhotoImage(file="images/logobrowse.png")
browselogolabel = Label (root , image = browselogo)

#browsebutton 
browsebutton = Button(root, text ="Browse", 
                      command = open_file,font = 20 ,height=1, width=9 , bg="#47a675")


#encrypt Button 
encryptButton = Button(root, text ="Encrypt", 
                      command = encryption,font = 20 ,height=1, width=9, bg="#47a675")


#decrypt Button 
decryptButton = Button(root, text ="Decrypt", 
                      command = decryption,font = 20 ,height=1, width=9 , bg="#47a675")

#placing all the elements 

bg.place(x=-10,y=0)
entry1.place(x=280,y=120)
keytitle.place(x=130,y=120)
keylabel.place(x=440,y=120)
browselabel.place(x=130,y=160)
browselogolabel.place(x=430,y=160)
browsebutton.place(x=355,y=220)
encryptButton.place(x=135,y=220)
decryptButton.place(x=245,y=220)

root.resizable(False, False )
root.mainloop()
