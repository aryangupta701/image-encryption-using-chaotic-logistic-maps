import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import logisticmap as lm
import initalvaluegen as initvalue
import realnum 
import numpy as np 
import encryptcalculate as cal 
from tkinter import filedialog
from tkinter import messagebox

def enc_success(imagename):
    messagebox.showinfo("Success","Encrypted Image: " + imagename)

def enc_success(imagename):
    messagebox.showinfo("Success","Decrypted Image: " + imagename)
    
def encryption(key,isEncrypt,file_name):
    img = mpimg.imread(file_name)
    plt.imshow(img)
    plt.show()
    height = img.shape[0]
    width = img.shape[1] 
    realnumbers = realnum.realnumgen(initvalue.initialX(key),3.9999,24) 
    y0 = initvalue.initialY(key, realnumbers) 
    chaoticmap = lm.generator(y0, 3.9999, height*width)
    z=0
    print(height,width) 
    enimg = np.zeros(shape=[height , width, 3], dtype = np.uint8)
    for i in range(height):
        for j in range(width):
            enimg[i,j] = cal.calcEncrypt(img[i,j],chaoticmap[z],key,isEncrypt)
            z+=1
    plt.imsave(file_name,enimg)
    if(isEncrypt):
        enc_success(file_name)
    else:
        dyc_success(file_name)
    plt.imshow(enimg)
    plt.show()
