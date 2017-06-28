# -*- coding: utf-8 -*-
import numpy as np
def somaC(x,j):
    soma=0
    for i in range(0,x.shape[0],1):
        soma=soma+x[i,j]
    return(soma)
def somaL(x,j):
    soma=0
    for j in range(0,x.shape[1],1):
        soma=soma+x[i,j]
    return(soma)
a=int(input('digite a dimenção da matriz:'))
l=int(input('digite a posiçãi da linha:'))
c=int(input('digite a posição da coluna:'))
x=np.zeros((a,a))
for i in range (0,x.shape[0],1):
    for j in range (0,x.shape[1],1):
        a[i,j]=int(input('peso:'))
R=somaL(x,l)+somaC(x,c)-(2*x[l,c])
print(R)


