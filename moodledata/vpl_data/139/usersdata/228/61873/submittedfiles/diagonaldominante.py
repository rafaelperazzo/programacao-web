# -*- coding: utf-8 -*-
import numpy as np

def diagonal(a):
    cont=0
    for i in range(0,a.shape[0],1):
        somal=0
        for j in range(0,a.shape[1],1):
            elementodp=a[i,i]
            if i!=j:
                somal=somal+a[i,j]
        if elementodp>somal:
            cont=cont+1
    return(cont)        
            
            

n=int(input('digite o número de elementos das linhas e colunas:'))
matriz=np.zeros((n,n))
for i in range(0,matriz.shape[0],1):
    for j in range(0,matriz.shape[1],1):
        matriz[i,j]=float(input('digite o elemento:'))
        
x=diagonal(matriz)
if x==n:
    print('SIM')
else:
    print('NAO')
    



