# -*- coding: utf-8 -*-
import numpy as np

p=0
n = int(input('Digite a dimensão n da matriz nxn: '))
matriz = np.empty([n,n])

for i in range(0,n,1):
    for j in range(0,n,1):
        matriz[i][j] = float(input('Digite o termo[%d][%d] da matriz: ' %((i+1),(j+1))))
        while(matriz[i][j] < 2):
            print('Número Inválido!')
            print('Tente um número maior ou igual a 2.')
            matriz[i][j] = float(input('Digite o termo [%d][%d] da matriz: ' %((i+1),(j+1))))
print(matriz)
for i in range(0,n,1):
    sum(matriz[i])
    print(sum(matriz[i]))
for i in range(0,n,1):
    for j in range(0,n,1):
        p += matriz[j][i]
        if j==(n-1):
            print(p)
        break
   
    
