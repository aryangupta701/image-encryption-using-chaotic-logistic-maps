def invert(val):
    val = val | 1<<7 
    return val
        
print(invert(23)) 