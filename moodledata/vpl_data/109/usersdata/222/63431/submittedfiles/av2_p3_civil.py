# -*- coding: utf-8 -*-
import numpy as np
def somai(matriz,x):
    soma=0
    for y in range(0,matriz.shape[1],1):
        soma=soma+matriz[x,y]
    return soma
def somaj(matriz,y):
    soma=0
    for x in range(0,matriz.shape[0],1):
        soma=soma+matriz[x,y]
    return soma
n=int(input('n:'))
x=int(input('x:'))
y=int(input('y:'))
matriz=n.pzeros((n,n))
for  x in range(0,matriz.shape[0],1):
    for y in range(0,matriz.shape[1],1):
        matriz[x,y]=int(input('peso:'))
s=somai((matriz,x)+somaj(matriz,y)-(2*matriz[x,y]))
print(s)
        

