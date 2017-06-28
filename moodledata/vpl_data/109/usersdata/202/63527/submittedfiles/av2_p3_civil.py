# -*- coding: utf-8 -*-
def peso (a,x,y):
    peso=0
    for i in range (0,a.shape[0],1):
        peso=peso+a[i,y]
    for j in range (0,a.shape[1],1):
        peso=peso+a[x,j]
    peso=peso-2*a[x,y]
    return peso
n=int(input('tamanho da matriz:'))    
p=int(input('i da posição:'))
m=int(input('j da posição:'))
import numpy as np
matriz=np.zeros((n,n))
for i in range (0,matriz.shape[0],1):
    for j in range (0,matriz.shape[1],1):
        matriz[i,j]=int(input('elemento:'))
print(peso(matriz,p,m))        
        


