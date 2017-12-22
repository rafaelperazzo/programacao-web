# -*- coding: utf-8 -*-
import numpy as np


def diagonalDominante(mat,n):
    for i in range(n):
        sLin = 0
        for j in range(n):
            if i != j:
                sLin += abs(mat[i][j])
        if abs(mat[i][i]) < sLin:
            return False
    return True
    
n= int(input('Digite n: '))
matriz= []
for i in range(0,n,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int('Digite um valor: '))
    matriz.append(linha)
    
if diagonalDominante(matriz,n):
    print('SIM')
else:
    print('NAO')


