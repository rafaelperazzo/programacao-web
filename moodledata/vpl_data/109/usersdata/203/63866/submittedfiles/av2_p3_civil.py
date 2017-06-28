# -*- coding: utf-8 -*-
import numpy as np
n=int(input('digite n: '))
a=np.zeros((n,n))
indice_x=int(input('digite a linha: '))
indice_y=int(input('digite a coluna: '))
soma_x=0
soma_y=0
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('digite valor: '))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        if i==indice_x:
            soma_x=soma_x+a[i,j]
        if j==indice_y:
            soma_y=soma_y+a[i,j]
peso=soma_x+soma_y-2*a[indice_x,indice_y]
print('%d'%peso)