# -*- coding: utf-8 -*-
import numpy as np
def somai(matriz,i):
    soma=0
    for j in range(0,matriz.shape[1],1):
        soma=soma+matriz[i,j]
    return soma
def somaj(matriz,j):
    soma=0
    for i in range(0,matriz.shape[0],1):
        soma=soma+matriz[i,j]
    return soma
def 
