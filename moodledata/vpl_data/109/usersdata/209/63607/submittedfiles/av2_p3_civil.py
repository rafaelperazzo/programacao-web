# -*- coding: utf-8 -*-
def peso(a,x,y):
    peso=0
    for i in range(0,a.shape[0],1):
        peso=peso+a[i,y]
    for j in range(0,a.shape[1],1):
        peso=peso+a[x,j]
    peso=peso-2*a[x,y]
    return peso
n=int(input('Digite o tamanho da matriz:'))
z=float(input('Digite o índice da posição:'))
a=z//1
b=(z%1)*10
import numpy as np
matriz=np.zeros((n,n))
for i in range(0,matriz.shape[0],1):
    for j in range(0,matriz.shape[1],1):
        matriz[i,j]=int(input('Digite um elemento:'))
print(peso(matriz,a,b))
