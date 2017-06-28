# -*- coding: utf-8 -*-
import numpy as np
def xmatriz(M):
    x=0
    cont=0
    soma=0
    parame=0
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            soma=soma+M[i,j]
        if soma==parame:
            x=soma
            contador=contador+1
            break
        parame=soma
        soma=0
    if contador==0:
        soma=0
        contador=0
        for i in range(1,M.shape[0]):
            for j in range(M.shape[1]):
                soma=soma+M[i,j]
            if soma==parame:
                x=soma
                contador=contador+1
                break
            parame=soma
            soma=0
    return(x)
def
a=int(input('digite o numero de elementos:'))
M=np.zeros((a,a))
for i in range(M.shape[0]):
    for j in tange(M.shape[1]):
        M[i,j]=int(input('elemento:'))
somaL=xmatriz(M)
print(somaL)

