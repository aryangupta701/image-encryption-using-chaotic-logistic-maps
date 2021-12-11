def calcEncrypt(pix , val, key , isEncrypt):
    pixel = pix.copy()
    print(val , pixel)
    if((val>=0.10 and val<0.13) or 
       (val>=0.34 and val<0.37) or
       (val>=0.58 and val<0.62) ):
        pixel[0] = ~(pixel[0])
        pixel[1] = ~(pixel[1])
        pixel[2] = ~(pixel[2])
        return pixel
        
    if((val>=0.13 and val<0.16) or 
       (val>=0.37 and val<0.40) or
       (val>=0.62 and val<0.66) ):
        pixel[0] = pixel[0]^ord(key[3])
        pixel[1] = pixel[1]^ord(key[4])
        pixel[2] = pixel[2]^ord(key[5])
        return pixel
        
    if((val>=0.16 and val<0.19) or 
       (val>=0.40 and val<0.43) or 
       (val>=0.66 and val<0.70) ):
        if isEncrypt :
            pixel[0] = (pixel[0] + ord(key[3]) + ord(key[4]))%256
            pixel[1] = (pixel[1] + ord(key[4]) + ord(key[5]))%256
            pixel[2] = (pixel[2] + ord(key[5]) + ord(key[3]))%256
            return pixel
        else :
            pixel[0] = pixel[0] - ord(key[3]) - ord(key[4]) + 256
            pixel[1] = pixel[1] - ord(key[4]) - ord(key[5])+ 256
            pixel[2] = pixel[2] - ord(key[5]) - ord(key[3])+ 256
            return pixel
             
    if((val>=0.19 and val<0.22) or
       (val>=0.43 and val<0.46) or
       (val>=0.70 and val<0.74) ):
        if isEncrypt : 
            pixel[0] = ~(pixel[0]^ord(key[3]))
            pixel[1] = ~(pixel[1]^ord(key[4]))
            pixel[2] = ~(pixel[2]^ord(key[5]))
            return pixel 
        else :
            pixel[0] = ~(pixel[0])^ord(key[3])
            pixel[1] = ~(pixel[1])^ord(key[4])
            pixel[2] = ~(pixel[2])^ord(key[5])
            return pixel
     
        #same as group 2 only inplace of key 3,4,5 , keys 6,7,8 are being used
    if((val>=0.22 and val<0.25) or  
       (val>=0.46 and val<0.49) or 
       (val>=0.74 and val<0.78) ):
        pixel[0] = pixel[0]^ord(key[6])
        pixel[1] = pixel[1]^ord(key[7])
        pixel[2] = pixel[2]^ord(key[8])
        return pixel
        
        #same as group 3 only inplace of key 3,4,5 , keys 6,7,8 are being used
    if((val>=0.25 and val<0.28) or 
       (val>=0.49 and val<0.52) or
       (val>=0.78 and val<0.82) ):
        if isEncrypt :
            pixel[0] = (pixel[0] + ord(key[6]) + ord(key[7]))%256
            pixel[1] = (pixel[1] + ord(key[7]) + ord(key[8]))%256
            pixel[2] = (pixel[2] + ord(key[8]) + ord(key[6]))%256
            return pixel
        else :
            pixel[0] = pixel[0] - ord(key[6]) - ord(key[7]) + 256
            pixel[1] = pixel[1] - ord(key[7]) - ord(key[8]) + 256
            pixel[2] = pixel[2] - ord(key[8]) - ord(key[6]) + 256
            return pixel
        
    if((val>=0.28 and val<0.31) or 
       (val>=0.52 and val<0.55) or
       (val>=0.82 and val<0.86) ):
        if isEncrypt:
            pixel[0] = ~(pixel[0]^ord(key[6]))
            pixel[1] = ~(pixel[1]^ord(key[7]))
            pixel[2] = ~(pixel[2]^ord(key[8]))
            return pixel
        else :
            pixel[0] = ~(pixel[0])^ord(key[6])
            pixel[1] = ~(pixel[1])^ord(key[7])
            pixel[2] = ~(pixel[2])^ord(key[8])
            return pixel
        
    if((val>=0.31 and val<0.34) or 
       (val>=0.55 and val<0.58) or
       (val>=0.86 and val<=0.90) ):
        return pixel;
    