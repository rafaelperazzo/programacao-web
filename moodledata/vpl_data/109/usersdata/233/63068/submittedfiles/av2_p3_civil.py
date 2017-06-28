# -*- coding: utf-8 -*-
import numpy as np
n=int(input('n: '))
matriz=np.zeros((n,n))
a=1
b=1
for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        matriz[i,j]=int(input('a[i,j]:  '))
somacolunas=0
for j in range(matriz.shape[1]):
    somacolunas=somacolunas+matriz[a,j]
somalinhas=0
for i in range(matriz.shape[0]):
    somalinhas=somalinhas+matriz[i,b]
somatotal=somalinhas+somacolunas-2*matriz[a,b]
print(somatotal)

