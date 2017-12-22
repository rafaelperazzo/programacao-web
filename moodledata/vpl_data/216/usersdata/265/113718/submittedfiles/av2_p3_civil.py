# -*- coding: utf-8 -*-
import numpy as np

m=int(input('digite a dimensao da matriz: '))
g=int(input('digite a linha: '))
h=int(input('digite a coluna: '))
a=np.zeros((m,m))

for i in range(0,m,1):
    for j in range(0,m,1):
        a[i,j]=int(input('digite o elemento: '))

def soma_linha(t,indice_linha):
    soma=0
    for j in range (0,t.shape[1],1):
        soma=soma+t[indice_linha,j]
    return(soma)

def soma_coluna(v,indice_coluna):
    soma=0
    for i in range(0,v.shape[0],1):
        soma=soma+v[i,indice_coluna]
    return(soma)

resultado=soma_linha(a,g)+soma_coluna(a,h)-(2*a[g,h])
print('%d' %resultado)
