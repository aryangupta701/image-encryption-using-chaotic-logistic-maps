def keygen(x,r,size):
    key=[]
    for i in range (size):
        x=r*x*(1-x) #logistic map
        key.append(int((x*pow(10,16))%256)) #key =  (x*10^16)%256
    return key 
    