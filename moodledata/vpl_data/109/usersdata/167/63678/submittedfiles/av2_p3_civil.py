# -*- coding: utf-8 -*-
import numpy as np
def peso(b,y,x):
    zv=[]
    zh=[]
    for i in range(0,b.shape[0],1):
        for j in range(0,a.shape[1],1):
            if j==x:
                zv.appen(b[i,j])
            if i==y:
                zh.append(b[i,j])
    w1=0
    w2=0
    for i in range(0,len(zv),1):
        w1=w1+zv[i]
    for i in range(0,len(zh),1):
        w2=w2+zh[i]
        
    w1=w1-b[y,x]
    w2=w2-b[y,x]
    wt=w1+w2
    return wt
    
n=input('digite o num lin/col:')
a=np.zerps((n.n))
y=input('digite a pos y:')
x=input('digite a pos x:')

for i in range(0,b.shape[0],1):
    for j in range(0,b.shape[1],1):
        b[i,j]=input('digite o el da matriz:')
        
print(b)
print(peso(b,y,x))