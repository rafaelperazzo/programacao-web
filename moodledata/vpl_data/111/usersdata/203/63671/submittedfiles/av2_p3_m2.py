# -*- coding: utf-8 -*-
import numpy as np
def soma_linha(a,i):
    soma=0
    for j in range(0,a.shape[1],1):
        soma=soma+a[i,j]
    return soma
def soma_coluna(a,j):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,j]
    return soma
def somatorio(a):
    if soma_linha(a,0)==soma_linha(a,1) or soma_linha(a,0)==soma_linha(a,2)
        soma_base=soma_linha(a,0)
    else:
        soma_base=soma_linha(a,1)
    
    