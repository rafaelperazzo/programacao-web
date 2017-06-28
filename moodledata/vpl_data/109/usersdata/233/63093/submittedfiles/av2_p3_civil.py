# -*- coding: utf-8 -*-
import numpy as np
n=int(input('n: '))
matriz=np.zeros((n,n))
x=int(input('x: '))
y=int(input('y: '))
for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        matriz[i,j]=int(input('matriz[i,j]:  '))
somacolunas=0
for j in range(matriz.shape[1]):
    somacolunas=somacolunas+matriz[x,j]
somalinhas=0
for i in range(matriz.shape[0]):
    somalinhas=somalinhas+matriz[i,y]
somatotal=somalinhas+somacolunas-2*matriz[x,y]
print('%.d'%somatotal)

