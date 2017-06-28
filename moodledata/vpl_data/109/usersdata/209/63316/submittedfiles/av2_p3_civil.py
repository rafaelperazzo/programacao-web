# -*- coding: utf-8 -*-
def peso(a,x,y):
    peso=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,y]
    for i in range(0,a.shape[1],1):
        soma=soma+a[x,i]
    return soma
n=int(input('Digite o tamanho da matriz:'))
a=int(input('Digite o i da posição:'))
b=int(input('Digite o j da posição:'))
import numpy as np
matriz=np.zeros((n,n))
for i in range(0,matriz.shape[0],1):
    for j in range(0,matriz.shape[1],1):
        matriz[i,j]=int(input('Digite um elemento:'))
print(peso(matriz,a,b))
