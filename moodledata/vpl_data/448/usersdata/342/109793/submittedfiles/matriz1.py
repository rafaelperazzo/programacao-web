# -*- coding: utf-8 -*-
m = int(input('insrira a quantidade de linhas: '))
n = int(input('insrira a quantidade de colunas: '))

matriz = []
for i in range (0,m,1):
    l = []
    for j in range (0,n,1):
        l.append(0)
    matriz.append(l)

for i in range (m-1,-1,-1):
  for j in range (n-1,-1,-1):
    matriz[i][j] = int(input('digite os elementos da matriz:'))

print(matriz)
