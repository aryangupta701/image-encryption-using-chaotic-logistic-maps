import initalvaluegen as initvalue
def realnumgen(x,r,size):
    arr=[]
    z=0
    while True:
        x=r*x*(1-x) #logistic map
        if(x>=0.1 and x<=0.9):
            arr.append(int(23*(x-0.1)/0.8) + 1 ) 
            z+=1 
        if(z==24):
            break;
    return arr 
    
realnumbers = realnumgen(initvalue.initialX("XAPR29f3BU"),3.9999,24)
print(initvalue.initialY("XAPR29f3BU", realnumbers))