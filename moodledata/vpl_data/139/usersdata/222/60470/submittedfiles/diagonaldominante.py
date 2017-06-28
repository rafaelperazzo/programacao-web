# -*- coding: utf-8 -*-
import numpy as np
def somadia(matriz):
    soma=0
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            if i==j:
                soma=soma+matriz[i,j]
    return soma
def somalinhas(matriz):
    soma=0
    for i in range(matriz.shape[0]):
        a=soma
        soma=0
        for j in range(matriz.shape[1]):
           soma=soma+matriz[i,j]
        if soma>a:
            soma=soma
        else:
            soma=a
    return soma
n=int(input('n:'))
matrizA=np.zeros((n,n))
for i in range(matrizA.shape[0]):
    for j in range(matrizA.shape[1]):
        matrizA[i,j]=int(input('numero:'))
if somadia(matrizA)>somalinhas(matrizA):
    print('SIM')
else:
    print('NAO')
