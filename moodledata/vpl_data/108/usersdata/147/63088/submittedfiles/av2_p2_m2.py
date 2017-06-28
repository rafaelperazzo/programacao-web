# -*- coding: utf-8 -*-
import numpy as np
def sl(r,i):
    sm=0
    for j in range(0,r.shape[1],1):
        sm=sm+r[i,j]
    return(sm)
def sc(r,j):
    sm=0
    for i in range(0,r.shape[0],1):
        sm=sm+r[i,j]
    return(sm)
tae=int(input('dimensão:'))
tif=int(input('posição linha:'))
seo=int(input('posição coluna:'))

r=np.zeros((tae,tae))
for i in range(0,r.shape[0],1):
    for j in range(0,r.shape[1],1):
        r[i,j]=int(input(peso:))
result=sl(r,tif)+sc(r,seo)-(2*r[tif,seo])
print(result)
