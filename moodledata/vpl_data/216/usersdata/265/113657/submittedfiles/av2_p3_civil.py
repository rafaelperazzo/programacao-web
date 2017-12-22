# -*- coding: utf-8 -*-
import numpy as np
dimensao=int(input('digite a dimensao da dimensaoatriz: '))
x=int(input('digite a linha: '))
y=int(input('digite a coluna: '))
a=np.zeros((dimensao,dimensao))
for i in range(0,dimensao,1):
    for j in range(0,dimensao,1):
        a[i,j]=int(input('digite o elemento: '))
def soma_linha(matriz,indice_elemento):
    soma=0
    for j in range (0,matriz.shape[1],1):
        soma=soma+a[indice_elemento,j]
    return(soma)
def soma_coluna(c,d):
    soma=0
    for i in range(0,c.shape[0],1):
        soma=soma+c[i,d]
    retrn(soma)
resultado=soma_linha(a,g)+soma_coluna(a,h)-(2*a[g,h])
print('%d' %resultado)
