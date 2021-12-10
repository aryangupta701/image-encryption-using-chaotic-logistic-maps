from tkinter import filedialog
from tkinter import *
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import logisticmap as lm
import initalvaluegen as initvalue
import realnum 

def encryption(key):
   # file = filedialog.askopenfile(mode='r')
   file = "DSC_6497.JPG"
   if file is not None:
       file_name=file
       img = mpimg.imread(file_name)
       height = img.shape[0]
       width = img.shape[1]
       realnumbers = realnum.realnumgen(initvalue.initialX("XAPR29f3BU"),3.9999,24)
       y0 = initvalue.initialY("XAPR29f3BU", realnumbers)
       chaoticmap = lm.generator(y0, 3.9999, height*width)
       z=0
       print(height,width)
       for i in range(height):
           for j in range(width):
               print(z,chaoticmap[z])
               z+=1


encryption("ABGSDOSD33")