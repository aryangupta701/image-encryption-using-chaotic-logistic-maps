
def encryptkey( key , size):
    k = list(key)
    r = 0
    for i in range(1,9):
        if ( (ord(key[i]) & (1<<1))!=0 ):
            bitval=1
        else:
            bitval=0
        r =  r + bitval*pow(2,i-1) 
    print(r)
    str = ""
    for x in range(size):
        str += chr(ord(k[x])^r)
    return str
