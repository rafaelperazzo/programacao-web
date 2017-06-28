# -*- coding: utf-8 -*-
import numpy as np







n=int(input('Número de elementos: '))
matriz=np.zeros((n,n))
for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        matriz[i,j]=int(input('Digite um elemento: '))

