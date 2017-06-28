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
            break
        parametro=soma
        soma=0
    if cont==0:
        soma=0
        cont=0
        for i in range(1,matriz.shape[0]):
            for j in range(matriz.shape[1]):
                soma=soma+matriz[i,j]
            if soma==parametro:
                m=soma
                cont=cont+1
                break
            parametro=soma
            soma=0
    return m
def 

n=int(input('Número de elementos: '))
matriz=np.zeros((n,n))
for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        matriz[i,j]=int(input('Digite um elemento: '))
        
somadalinha=m_da_matriz(matriz)


