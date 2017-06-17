# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
import numpy as np
a=3
b=2
matriz=np.zeros((a,b))
for i in range(0,matriz.shape[0],1):
    for j in range(0,matriz.shape[1]):
        matriz[i,j]=int(input('elemento: '))
print(matriz[2][0])
print(sum(matriz))




