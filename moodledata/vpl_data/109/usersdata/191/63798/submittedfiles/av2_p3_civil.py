# -*- coding: utf-8 -*-
import numpy as np
def peso(a,b,c):
    c=[]
    d=[]
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if j==c:
                c.append(a[i,j])
            if i==b:
                d.append(a[i,j])
    e1=0
    e2=0
    for i in range(0,len(c),1):
        e1=e1+c[i]
    for i in range(0,len(d),1):
        e2=e2+d[i]
        
    e1=e1-a[b,c]
    e2=e2-a[b,c]
    et=e1+e2
    return et
    
n=int(input('digite o num lin/col:'))
b=np.zeros((n,n))
w=input('digite a pos w:'))
z=input('digite a pos z:'))

for i in range(0,b.shape[0],1):
    for j in range(0,b.shape[1],1):
        b[i,j]=input('digite a matriz:'))
        
print(b)
print(peso(a,b,c))


