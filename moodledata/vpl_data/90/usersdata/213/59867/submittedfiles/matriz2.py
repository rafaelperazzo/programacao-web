# -*- coding: utf-8 -*-
def somaDasLinhas(matriz):
    somatorioLinha=[]
    for i in range(0,matriz.shape[0],1):
        soma=0
        for j in range(0,matriz.shape[1],1):
            soma=soma+matriz[i,j]
        somatorioLinha.append(soma)
    for k in range(0, len(somatorioLinha),1):
        if somatorioLinha[0]!=somatorioLinha[i]:
            return (False)
        else:
            return(somatorioLinha[0])

def somaDasColunas(matriz):
    somatorioColuna=[]
    for j in range(0,matriz.shape[1],1):
        soma=0
        for i in range(0,matriz.shape[0],1):
            soma=soma+matriz[i,j]
        somatorioColuna.append(soma)
    for k in range(0, len(somatorioColuna),1):
        if somatorio[0]!=somatorio[i]:
            return (False)
        else:
            return(somatorioColuna[0])

def somaDiagonalPrincipal(matriz):
    soma=0
    for i in range(0,matriz.shape[0],1):
        soma=soma+matriz[i,i]
    return(soma)

def somaDiagonalSecundaria(matriz):
    soma=0
    for i in range(0,matriz.shape[0],1):
        soma=soma+[matriz.shape[0]-i-1,i]
    return(soma)

import numpy as np
n= int(input('Informe a quantidade de linhas e colunas da matriz: '))
matriz=np.zeros((n,n))

for i in range(0,matriz.shape[0],1):
    for j in range(0,matriz.shape[1],1):
        matriz[i,j]=int(input('Informe o elemento: '))

valorLinha=somaDasLinhas(matriz)
valorColuna=somaDasColunas(matriz)
valorDiagonalPrincipal=somaDiagonalPrincipal(matriz)
valorDiagonalSecundaria=somaDiagonalSecundária(matriz)

if valorLinha==False or valorColuna==False:
    print('N')
else:
    if valorLinha==valorColuna==valorDiagonalPrincipal==valorDiagonalSecundaria:
        print('S')
    else:
        print('N')
