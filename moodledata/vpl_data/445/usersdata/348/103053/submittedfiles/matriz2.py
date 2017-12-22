# -*- coding: utf-8 -*-
import numpy as np

n = int(input( ' informe a quantidade de linhas/colunas: '))

matriz = np.empty([n,n])

for i in range (0,n,1):
    for j in range (0,n,1):
        matriz[i][j] = int(input('informe o %d° linha e o %d° coluna: ' %((i+1),(j+1))))

#diagonal principal
m = 0
for k in range (n):
    m = m + matriz[k][k]

#diagonal secundario
s =  0
for l in range (n):
    s = s + matriz[l][n-1-l]
if (s != m):
    print("N")
    exit()
    
#colunas
for h in range (n):
    s = 0
    for g in range (n):
        s = s + matriz[g][h]
    if (s != m):
        print("N")
        exit()
print('S')