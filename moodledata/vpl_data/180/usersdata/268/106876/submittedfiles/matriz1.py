# -*- coding: utf-8 -*-
import numpy as np

linhas= int(input('Digite linhas :' ))
colunas= int(input('Digite colunas: '))

a= np.zeros((linhas,colunas))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j] = int(input('Digite o elemento:'))

def soma_linha (b,c):
    soma=0
    for j in range (0,b.shape[1],1):
        soma= soma + a[c,j]
    return(soma)

matriz=[]

for i  in range (0,shape[0],1):
    if soma_linha(a,i) != 0:
        matriz.append(a[i,:])
print(matriz)
