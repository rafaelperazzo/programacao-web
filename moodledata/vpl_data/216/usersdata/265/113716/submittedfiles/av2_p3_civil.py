# -*- coding: utf-8 -*-
import numpy as np

dimensao=int(input('digite a dimensao da matriz: '))
x=int(input('digite a linha: '))
y=int(input('digite a coluna: '))
a=np.zeros((dimensao,dimensao))

for i in range(0,dimensao,1):
    for j in range(0,dimensao,1):
        a[i,j]=int(input('digite o elemento: '))

def soma_linha(matriz,indice_linha):
    soma=0
    for j in range (0,matriz.shape[1],1):
        soma=soma+matriz[indice_linha,j]
    return(soma)

def soma_coluna(matriz,indice_coluna):
    soma=0
    for i in range(0,matriz.shape[0],1):
        soma=soma+matriz[i,indice_coluna]
    return(soma)

resultado=soma_linha(a,x)+soma_coluna(a,y)-(2*a[x,y])
print('%d' %resultado)
