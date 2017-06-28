# -*- coding: utf-8 -*-
import numpy as np
def somasecundaria(matriz):
    soma=0
    j=0
    i=matriz.shape[0]-1
    while j<matriz.shape[1]:
        soma=soma+matriz[i,j]
        j=j+1
        i=i-1
    return soma
def somaprincipal(matriz):
    soma=0
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            if i==j:
                soma=soma+matriz[i,j]
    return soma
    

