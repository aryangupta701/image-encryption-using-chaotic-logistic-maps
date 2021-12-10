import logisticmap as lm
import initalvaluegen as initvalue
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import numpy as np 
import realnum
#reading an image 

x="python.bmp"
img = mpimg.imread(x)
plt.imshow(img)
plt.show 


#generating chaotic keys
height = img.shape[0]
width = img.shape[1]
inputkey = "B33EF89AF3"
key = lm.generator(initvalue.initial(inputkey),3.9999,height*width)
realnumbers = realnum.realnumgen(initvalue.initialX(inputkey),3.9999,24)
print(key)
print(realnumbers)
#encryption substitution wiith XOR
z=0
enimg = np.zeros(shape=[height , width, 3], dtype = np.uint8)
for i in range(height):
    for j in range(width):
        enimg[i,j] = img[i,j]^key[z]
        z+=1

plt.imshow(enimg)
plt.show()
plt.imsave(x,enimg)