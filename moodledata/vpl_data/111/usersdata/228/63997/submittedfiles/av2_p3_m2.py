# -*- coding: utf-8 -*-
import numpy as np
n=int(input('digite o tamanho da matriz :'))
matriz=np.zeros((n,n))
for i in range(0,matriz.shape[0],1):
    for j in range(0,matriz.shape[1]):
        matriz[i,j]=float(input('digite o elemento :'))
        
soma=0        
for j in range(0,matriz.shape[1],1):
    soma=soma+matriz[1,j]
 
cont1=0   
L=[]
for j in range(0,matriz.shape[1],1):
    somaL=0
    for i in range(0,matriz.shape[1],1):
        if i!=j:
            cont1=cont1
            somaL=somaL+matriz[i,j]
            L.append(somaL)
contl=0
for i in range(o,len(L)-1,1):
    if L[i]!=L[i+1]:
        z=L[i]=L[i-1]
        contl=contl
    else:
        contl=contl+1

x=contl
cont2=0
C=[]   
for i in range(0,matriz.shape[0],1):
    somaC=0
    for j in range(0,matriz.shape[1],1):
        if i!=j:
            cont2=cont2
            somaC=somaC+matriz[i,j]
            C.append(somaC)
            
contc=0
for i in range(o,len(C)-1,1):
    if C[i]!=C[i+1]:
        contl=contl
    else:
        contl=contl+1

y=contc            

print((matriz[x,y]-z))
print(matriz[x,y])
