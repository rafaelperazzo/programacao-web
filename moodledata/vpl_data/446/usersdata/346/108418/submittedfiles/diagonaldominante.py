# -*- coding: utf-8 -*-

def diagonalDominante(matriz,n):
    for i in range(n):
        aLin = 0
        for j in range(n):
            if i != j:
                sLin += abs(matriz[i][j])
        if abs(matriz[i][i]) < sLin:
            return print('NAO')
    return print('SIM')
    
n= int(input())
matriz= []
diagonalDominante(matriz,n)
