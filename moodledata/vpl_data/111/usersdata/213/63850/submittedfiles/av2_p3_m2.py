# -*- coding: utf-8 -*-
def somaDiagonalPrincipal(matriz):
    somaDP=0
    for i in range(0,matriz.shape[0],1):
        for j in range(0,matriz.shape[1],1):
            if i==j:
                somaDP=somaDP+matriz[i,j]
    return (somaDP)
    
def somaLinha(matriz):
    somaDP=somaDiagonalPrincipal(matriz)
    contador=0
    for i in range(0,matriz.shape[0],1):
        somaLinha=0
        for j in range(0,matriz.shape[1],1):
            somaLinha=somaLinha+matriz[i,j]
                if somaDP==somaLinha:
                    contador=contador+1
                else:
                    linhaErro==contador
    return(linhaErro)

def somaColuna(matriz):
    somaDP=somaDiagonalPrincipal(matriz)
    contador=0
    for j in range(0,matriz.shape[1],1):
        somaColuna=0
        for i in range(0,matriz.shape[0],1):
            somaColuna=somaColuna+matriz[i,j]
                if somaDP==somaColuna:
                    contador=contador+1
                else:
                    colunaErro==contador
    return(colunaErro)

def testeErro(matriz):
    somaDP=somaDiagonalPrincipal(matriz)
    for i in range(0,matriz.shape[0],1):
        for j in range(0,matriz.shape[1],1):
            for i in range(matriz[linhaErro,colunaErro],100,1):
                
                    

import nump as np
n=int(input('Informe a quantidade de linhas e colunas da matriz: '))
matriz=np.zeros((n,n))
for i in range(0,matriz.shape[0],1):
    for j in range(0,matriz.shape[1],1):
        matriz[i,j]=int(input('Informe os elementos da matriz: '))

def

