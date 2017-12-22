# -*- coding: utf-8 -*-

def diagonalDominante(mat,n):
    for i in range(n):
        sLin = 0
        for j in range(n):
            if i != j:
                sLin += abs(mat[i][j])
        if abs(mat[i][i]) < sLin:
            return print('NAO')
    return print('SIM')
    
n= int(input())
matriz= []
for i in range(0,n,1):
    linha=[]
    for j in range(0,n,1):
        linha.append('Digite um valor: ')
    matriz.append(linha)
    
print(diagonalDominante(matriz,n))
