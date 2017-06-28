# -*- coding: utf-8 -*-
import numpy as np
def L(x):
    L=[]
    for i in range(0,x.shape[0],1):
        s=0
        for j in range(0,x.shape[1],1):
            s=s+x[i,j]
        L.append(s)
    return(L)
def C(x):
    C=[]
    for j in range(0,x.shape[1],1):
        s=0
        for i in range(o,x.shape[0],1):
            s=s+x[i,j]
        C.append(s)
    return(C)
def indice(y):
    for i in range (o,len(y),1):
        contador=0
        for j in range (0,len(y),1):
            if y[i]==y[j]:
                contador=contador+1
        if contador==1:
            return i
def num(lista,indice):
    for i in range(0,len(lista),1):
        if i!=indice:
            num=lista[indice]-lista[i]
            return(num)
a=int(input('digite o tamanho da matriz:'))
x=np.zeros((a,a))
for i in range (0,x.shape[0],1):
    for j in range(0,x.shape[1],1):
        x[i,j]=int(input('digite os termos da matriz:'))
L=L(x)
C=C(x)
t=indice(L)
r=indice(C)
z=x[l,c]
n=z-(num(L,t))
print('%d.'%n)
print('%d.'%z)
        



