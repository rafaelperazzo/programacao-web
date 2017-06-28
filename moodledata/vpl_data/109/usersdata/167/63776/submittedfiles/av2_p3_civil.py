# -*- coding: utf-8 -*-
import numpy as np

n=input('digite o num lin/col:')
a=np.zeros((n,n))

x=input('digite a pos x:')
y=input('digite a pos y:')

def peso(a,x,y):
    lv=[]
    lh=[]
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if j==y:
                lv.append(a[i,j])
            if i==x:
                lh.append(a[i,j])
    
    p1=0
    p2=0
    for i in range(0,len(lv),1):
        p1=p1+zv[i]
    for i in range(0,len(lh),1):
        p2=p2+lh[i]
        
    p1=p1-a[y,x]
    p2=p2-a[y,x]
    pt=p1+p2
    return pt
    

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('digite o el da matriz:')
        
print(peso(a,x,y))