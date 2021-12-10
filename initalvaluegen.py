#generated the inital valye of X logistic map
def initialX(inputkey):
    #generating the value of X01
    x01 = 0
    z=0
    for i in range(4,7):
        temp = ord(inputkey[i])
        for j in range(8):
            if (temp & (1<<j)!=0):
                bitval=1
            else:
                bitval=0
            x01 = x01 + bitval*pow(2,z)
            z+=1 
    x01 = x01/pow(2,24)
    #generating the value of X02 
    x02=0
    for i in range(6,9):
        temp = ord(inputkey[i])
        x02 = x02 + temp/96
    return (x01+x02)%1

#generated the inital valye of Y logistic map

def initialY(inputkey , p):
    #generating the value of Y01
    y01 = 0
    z=0
    b2=[]
    for i in range(3):
        temp = ord(inputkey[i])
        for j in range(8):
            if (temp & (1<<j)!=0):
                bitval=1
            else:
                bitval=0
            b2.append(bitval)
            y01 = y01 + bitval*pow(2,z)
            z+=1 
    y01 = y01/pow(2,24)
    #generating the value of Y02
    y02=0 
    for i in range(24):
        y02 = y02 + b2[p[i]]*pow(2,i)
    y02 = y02/pow(2,24)
    return (y01+y02)%1


