import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import logisticmap as lm
import initalvaluegen as initvalue
import realnum 
import numpy as np 
import encryptcalculate as cal 

def encryption(key,isEncrypt):
    # file = filedialog.askopenfile(mode='r')
    file = "sample_640×426.bmp"
    if file is not None:
        file_name=file
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
                enimg[i,j] = cal.calcEncrypt(img[i,j],chaoticmap[z] ,key,isEncrypt)
                z+=1
        plt.imsave(file,enimg)
        plt.imshow(enimg)
        plt.show()


encryption("XAPR29f3BU",False)