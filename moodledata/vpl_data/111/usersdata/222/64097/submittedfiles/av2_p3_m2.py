# -*- coding: utf-8 -*-
import numpy as np
def somai(matriz,i):
    soma=0
    for j in range(0,matriz.shape[1],1):
        soma=soma+matriz[i,j]
    return soma
def somaj(matriz,j):
    soma=0
    for i in range(0,matriz.shape[0],1):
        soma=soma+matriz[i,j]
    return soma
def inicial(matriz):
    if somai(matriz,0)==somai(matriz,1) or somai(matriz,0)==somai(matriz,2):
        somageral=somai(matriz,0)
    else:
        somageral=somai(matriz,1)
        for i in range(0,matriz.shape[0],1):
            if somai(matriz,i)!=somageral:
                modificadoi=i
        for j in range(0,matriz.shape[1],1):
            if somaj(matriz,j)!=somageral:
                modificadoj=j
            modificado=matriz[modificadoi,modificadoj]
        return modificado
def x(matriz):
    if somai(matriz,0)==somai(matriz,1) or somai(matriz,0)==somai(matriz,2):
        somageral=somai(matriz,0):
    else: 
        somageral=somai(matriz,1)
        for i in range(0,matriz.shape[0],1):
            if somai(matriz,i)!=somageral:
                somamodificada=somai(matriz,i)
s=somamodificada-somageral
return s
n=int(input('n:'))
matriz=np.zeros((n,n))
for i in range(0,matriz.shape[0],1):
    for j in range(0,matriz.shape[1],1):
        matriz[i,j]=int(input('valor:'))
print(int(inicial(matriz)-x(matriz)))
                
                
        
        
