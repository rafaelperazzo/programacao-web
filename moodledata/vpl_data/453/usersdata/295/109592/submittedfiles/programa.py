# -*- coding: utf-8 -*-
import numpy as np
matriz = []
n = int(input("Digite o tamanho da matriz: "))
while not n>=3:
    n = int(input("Digite o tamanho da matriz: "))
for i in range(0,n,1):
    linhas = []
    for j in range(0,n,1):
        linhas.append(int(input("Digite o valor da linha e coluna :")))
    matriz.append(linha)
    
ntrans = np.empty([n,n])
for j in range(0,n,1):
    for i in range(0,n,1):
        ntrans[j][i]=matriz[i][j]
        
st = sum(matriz[0]) + sum(ntrans[0]) - 2*(matriz[0][0])
for i in range(0,n,1):
    for j in range(0,n,1):
        if st > sum(matriz[i]) + sum(ntrans[j]) - 2*(matriz[i][j]):
            st = st
        else:
            st = sum(matriz[i]) + sum(ntrans[j]) - 2*(matriz[i][j])
print(st)

    
