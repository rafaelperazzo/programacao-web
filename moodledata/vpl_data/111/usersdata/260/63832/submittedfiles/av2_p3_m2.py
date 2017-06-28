# -*- coding: utf-8 -*-
import numpy as np
d=int(input("digite a dimensão da matriz desejada"))
matriz=np.zeros( (d,d) )
for i in range (0,matriz.shape[0],1):
    for j in range (0,matriz.shape[1],1):
        matriz[i,j]= int(input("digite o valor do elemento da matriz:"))
        


