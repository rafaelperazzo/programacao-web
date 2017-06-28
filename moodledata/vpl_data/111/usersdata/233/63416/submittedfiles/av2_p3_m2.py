# -*- coding: utf-8 -*-
import numpy as np
def m_da_matriz(matriz):
    m=0
    cont=0
    soma=0
    parametro=0
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            soma=soma+matriz[i,j]
        if soma==parametro:
            m=soma
            cont=cont+1
            return m
            break
        parametro=soma
    if cont==0:
        soma=0
        cont=0
        for i in range(1,matriz.shape[0]):
            for j in range(matriz.shape[1]):
                soma=soma+matriz[i,j]
            if soma==parametro:
                m=soma
                cont=cont+1
                return m
                break
            parametro=soma

n=int(input('Número de elementos: '))
matriz=np.zeros((n,n))
for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        matriz[i,j]=int(input('Digite um elemento: '))
        
m=m_da_matriz(matriz)
print(m)

