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
t=int(input('dimensão:'))
ti=int(input('posição linha:'))
s=int(input('posição coluna:'))

r=np.zeros((t,t))
print(r)
for i in range(0,r.shape[0],1):
    for j in range(0,r.shape[1],1):
        r[i,j]=int(input('termo:'))
        print(r)
result=sl(r,ti)+sc(r,s)-(2*r[ti,s])
print(result)


