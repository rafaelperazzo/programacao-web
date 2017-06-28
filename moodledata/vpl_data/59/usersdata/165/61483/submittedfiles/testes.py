# -*- coding: utf-8 -*-
def naocomum(a,b):
    c=[]
    for i in range(0,len(a),1):
        if a[i] not in b:
            c.append(a[i]):
    for j  in range(0,len(b),1):
        if b[i] not in a and b[i] not in b:
            c.append(b[i])
    
    return(c)
    

a=[1,5,3,2,4,5,6]
b=[6,5,3,2,2,7,9]
l=naocomum(a,b)
print(l)
