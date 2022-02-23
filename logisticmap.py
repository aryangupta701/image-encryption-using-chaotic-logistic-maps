#logistic map to generate values between 0.1 and 0.9 

def generator(x,r,size):
    map=[]
    z=0
    while True:
        x=r*x*(1-x) #logistic map
        if(x>=0.1 and x<=0.9):
            map.append(x) #key =  (x*10^16)%256
            z+=1
            if(z==size):
                break;
    return map

