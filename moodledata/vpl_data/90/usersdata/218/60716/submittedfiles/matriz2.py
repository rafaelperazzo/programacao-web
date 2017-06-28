# -*- coding: utf-8 -*-
import numpy as np
def somas (a):
    lista=[]
    cont=0
    for i in range (0,a.shape[0],1):
        cont=0
        for j in range (0,a.shape[1],1):
            cont=cont+a[i,j]
        lista.append(cont)
    for j in range (0,a.shape[1],1):
        cont=0
        for i in range (0,a.shape[0],1):
            cont=cont+a[i,j]
        lista.append(cont)
    cont=0    
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if i==j:
                cont=cont+a[i,j]
    lista.append(cont)
    i=0
    j=a.shape[1]-1
    cont=0
    while j>=0:
        cont=cont+a[i,j]
        i=i+1
        j=j-1
    lista.append(cont)
    return(lista)     
n=int(input('digite as dimensões da matriz quadrada:'))
a=np.zeros((n,n))
for i in range (0,a.shape[0],1):
    for j in range (0, a.shape[1],1):
        a[i,j]=float(input('digite o elemento:'))
print(somas(a))