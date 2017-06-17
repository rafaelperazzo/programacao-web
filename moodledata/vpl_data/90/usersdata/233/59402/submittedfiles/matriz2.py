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
def somalinhas(matriz):
    soma=0
    for i in range(matriz.shape[0]):
        a=soma
        cont=0
        soma=0
        for j in range(matriz.shape[1]):
            soma=soma+matriz[i,j]
        if soma>a:
            cont=cont+1
    if cont>1:
        return (10101010101010101010101)
    else:
        return soma
def somacolunas(matriz):
    soma=0
    for j in range(matriz.shape[1]):
        a=soma
        cont=0
        soma=0
        for i in range(matriz.shape[0]):
            soma=soma+matriz[i,j]
        if soma>a:
            cont=cont+1
    if cont>1:
        return (10101010101010101010101)
    else:
        return soma
n=int(input('Digite o número de linhas e colunas da matriz: '))
matriza=np.zeros((n,n))
for i in range(matriza.shape[0]):
    for j in range(matriza.shape[1]):
        matriza[i,j]=int(input('Digite um número: '))
cont=0
if somasecundaria(matriza)!=somaprincipal(matriza) or somasecundaria(matriza)!=somalinhas(matriza) or somasecundaria(matriza)!=somacolunas(matriza):
    cont=cont+1
elif somaprincipal(matriza)!=somalinhas(matriza) or somaprincipal(matriza)!=somacolunas(matriza):
    cont=cont+1
elif somacolunas(matriza)!=somalinhas(matriza):
    cont=cont+1
if cont>0:
    print('N')
else:
    print('S')

