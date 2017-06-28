# -*- coding: utf-8 -*-
import numpy as np
n=int(input('digite a dimensão da matriz:'))
indiceI=int(input('digite o indice da linha'))
indiceJ=int(input('digite o indice da coluna'))

matriz=np.zeros((n,n))
for i in range(0,matriz.shape[0],1):
    for j in range(0,matriz.shape[1],1):
        matriz[i,j]=float(input('digite o elemento:'))
        
def somaLina(matriz,x,y):
    somaL=0        
    for j in range(0,matriz.shape[1],1):
        if matriz[x,j]==matriz[x,y]:
            somaL=somaL
        else:
            somaL=somaL+matriz[x,j]
    return(somaL)    

def somaColuna(matriz,y,x):
    somaC=0
    for i in range(0,matriz.shape[0],1):
        if matriz[i,y]==matriz[x,y]:
            somaC=somaC
        else:
            somaC=somaC+matriz[i,y]
    return(somaC)

resultado=somaLina(matriz,indiceI)+somaColuna(matriz,indiceJ)
print(resultado)
        
