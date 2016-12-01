# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

dim = input ('Dimensão da matriz desejada:')
a=np.zeros((dim,dim))
# Indices da matriz
x = input('Indices Linha:')
y = input('Indices Colunas:')

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input('Elemento:')
        
#Definir abaixo a função que calcula o peso:
def peso(matriz,i,j):
    linhas=sum(matriz[i,:])-matriz[i,j]
    colunas=sum(matriz[:,j]-matriz[i,j]
    peso=linhas+colunas
    return peso
print peso(a,x,y)
