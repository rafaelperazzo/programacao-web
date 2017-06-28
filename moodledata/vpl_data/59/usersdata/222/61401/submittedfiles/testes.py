
def angulosexasimal(L):
    dec=[]
    for i in range(0,len(L),1):
        dec.append(L[i]+(L[i+1]/60)+(L[i+2]/3600))
    return dec
    
L=[23,37,28]
print(dec)
    