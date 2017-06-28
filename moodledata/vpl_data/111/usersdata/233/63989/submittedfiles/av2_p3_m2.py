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
    linha=-1
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            soma=soma+matriz[i,j]
        linha=linha+1
        if soma!=valor:
            break
        soma=0
    return linha
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

n=int(input('Número de elementos: '))
matriz=np.zeros((n,n))
for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        matriz[i,j]=int(input('Digite um elemento: '))

somacerta=m_da_matriz(matriz)
linhaerrada=linhaerrada(matriz,somacerta)
print(linhaerrada)
diferença=(somacerta)-valor_matriz_errada(matriz,linhaerrada) 
a=linhaerrada(matriz,somacerta)
b=colunaerrada(matriz,somacerta)
print(matriz[a,b])
print(matriz[linhaerrada(matriz,somacerta),colunaerrada(matriz,somacerta)]+diferença)

