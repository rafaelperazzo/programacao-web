# -*- coding: utf-8 -*-

def diagonalDominante(matriz,n):
    for i in range(n):
        aLin = 0
        for j in range(n):
            if i != j:
                aLin += abs(matriz[i][j])
        if abs(matriz[i][i]) < sLin:
            return print('NAO')
    return print('SIM')
    
n= int(input())
matriz= []
for i in range(0,n,1):
    linha=[]
    for j in range(0,n,1):
        linha.append('Digite um valor: ')
    matriz.append(linha)
    
diagonalDominante(matriz,n)
