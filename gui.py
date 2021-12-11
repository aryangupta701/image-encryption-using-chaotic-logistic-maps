def pass_alert():
    tkMessageBox.showinfo("Password Alert","Please enter a password.")

def enc_success(imagename):
    tkMessageBox.showinfo("Success","Encrypted Image: " + imagename)

# image encrypt button event
def image_open():
    global file_path_e
    enc_pass = passg.get()
	if(enc_pass == "sdff" ): 
        s_alert()
    else: 
        sword = hashlib.sha256(enc_pass).digest()
        ename = tkFileDialog.askopenfilename()
        e_path_e = os.path.dirname(filename)
        rypt(filename,password)
 
# image decrypt button event
def cipher_open():
    global file_path_d
	dec_pass = passg.get()
	if dec_pass == "":
        pass_alert()
	else:
        password = hashlib.sha256(dec_pass).digest()
        ename = tkFileDialog.askopenfilename()
        e_path_d = os.path.dirname(filename)
        rypt(filename,password)
	
class App:
    def __init__(self, master):
	    global passg
	    title = "Image Encryption"
	    author = "Made by Aditya"
	    msgtitle = Message(master, text =title)
	    msgtitle.config(font=('helvetica', 17, 'bold'), width=200)
	    msgauthor = Message(master, text=author)
	    msgauthor.config(font=('helvetica',10), width=200)
	
	    canvas_width = 200
	    canvas_height = 50
	    w = Canvas(master,
	           width=canvas_width,
	           height=canvas_height)
	    msgtitle.pack()
	    msgauthor.pack()
	    w.pack()
	
        passlabel = Label(master, text="Enter Encrypt/Decrypt Password:")
	    passlabel.pack()
	    passg = Entry(master, show="*", width=20)
	    passg.pack()
	
	    self.encrypt = Button(master,
	                         text="Encrypt", fg="black",
	                         command=image_open, width=25,height=5)
	    self.encrypt.pack(side=LEFT)
	    self.decrypt = Button(master,
	                         text="Decrypt", fg="black",
	                         command=cipher_open, width=25,height=5)
	    self.decrypt.pack(side=RIGHT)



# ------------------ MAIN -------------#
root = Tk()
root.wm_title("Image Encryption")
app = App(root)
root.mainloop()
