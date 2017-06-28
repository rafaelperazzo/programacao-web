# -*- coding: utf-8 -*-
import numpy as np
def peso(a,x,y):
    vert=[]
    hor=[]
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if j==y:
                vert.append(a[i,j]):
            if i==x:
                hor.append(a[i,j]):
    p1=0
    p2=0
    for i in range (0,len(vert),1):
        p1=p1+vert[i]
    for i in range (0,len(hor),1):
        p1=p1+hor[i]
    p1=p1-a[x,y]
    p2=p2-a[x,y]
    ptotal=p1+p2
    return ptotal
n=int(input('Tamanho da matriz:'))
x=int(input('x:'))
y=int(input('y:'))

a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[0],1):
        a[i,j]=int(input('Valor:'))
valor=peso(a,x,y)
print('%.d'%valor)

