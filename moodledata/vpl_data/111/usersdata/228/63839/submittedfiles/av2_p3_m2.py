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
    


for j in range(0,matriz.shape[1],1):
    somaL=0
    cont=0
    for i in range(0,matriz.shape[1],1):
        if i!=j:
           somaL=somaL+matriz[i,j]
           if somaL!=soma:
               x=abs(somaL-soma)
        else:
            cont=cont+1
     y=cont      
   
for i in range(0,matriz.shape[0],1):
    somaC=0
    cont=0
    for j in range(0,matriz.shape[1],1):
        if i!=j:
           somaC=somaC+matriz[i,j]
           if somaC!=soma:
               x=abs(somaL-soma)
        else:
            cont=cont+1   
    z=cont

print
print(matriz[y,z])
