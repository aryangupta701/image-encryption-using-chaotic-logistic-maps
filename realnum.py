#to generate a array of length size using logistic map in the range 0-size

def realnumgen(x,r,size):
    arr=[]
    z=0
    while True:
        x=r*x*(1-x) #logistic map
        if(x>=0.1 and x<=0.9):
            arr.append(int((size-1)*(x-0.1)/0.8) + 1 ) 
            z+=1 
        if(z==size):
            break;
    return arr 
