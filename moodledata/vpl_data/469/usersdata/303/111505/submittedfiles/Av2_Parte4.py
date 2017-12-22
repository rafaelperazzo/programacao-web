# -*- coding: utf-8 -*-
matriz=[]
m=int(input('Digite a ordem da matriz:'))
for i in range(0,m,1):
    linha=[]
    for j in range(0,m,1):
        linha.append(int(input('Digite a linha/coluna:')))
    matriz.append(linha)

linhaS=[]
for i in range(0,m,1):
    sl=0
    for j in range(0,m,1):
        sl+=matriz[i][j]
    linhaS.append(sl)
print(linhaS)
print(matriz)
        