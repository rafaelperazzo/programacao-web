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
def linhaerrada(matriz,valor):
    soma=0
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
        soma=soma+matriz[i,j]
    if soma!=valor:
        return i
        break
    soma=0
def colunaerrada(matriz,valor):
    soma=0
    for j in range(matriz.shape[1]):
        for j in range(matriz.shape[0]):
            soma=soma+matriz[i,j]
    if soma!=valor:
        return j
        break
    soma=0
def valor_matriz_errada(matriz,a):
    soma=0
    for j in range(matriz.shape[1]):
        soma=soma+matriz[a,j]
    return soma
somacerta=m_da_matriz(matriz)
diferença=(somacerta)-valor_matriz_errada(matriz,somacerta) 
n=int(input('Número de elementos: '))
matriz=np.zeros((n,n))
for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        matriz[i,j]=int(input('Digite um elemento: '))
valor=m_da_matriz(matriz)
print(matriz[(linhaerrada(matriz,somacerta),colunaerrada(matriz,somacerta)])
print(matriz[(linhaerrada(matriz,somacerta),colunaerrada(matriz,somacerta)]+diferença)

