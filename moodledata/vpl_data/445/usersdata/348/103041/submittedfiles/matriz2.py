# -*- coding: utf-8 -*-

n = int(input( ' informe a quantidade de linhas/colunas: '))

matriz = np.empty([n,n])

for i in range (0,n,1):
    for j in range (0,n,1):
        matriz[i][j] = int(input('informe o %d° linha e o %d° coluna: ' %((i+1),(j+1))))
print(matriz)
