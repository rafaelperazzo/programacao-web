# -*- coding: utf-8 -*-
n = int(input('Digite a ordem da matriz: '))
matriz = []
for i in range(0,n,1):
    linha = []
    for j in range(0,n,1):
        linha.append(int(input('Digite um elemento da matriz: ')))
    matriz.append(linha)
    
p = 0
for i in range(0,n,1):
    cont = 0
    for j in range(0,n,1):
        cont += matriz[i][j]
    if cont > matriz[i][i]:
        p = p + 1
        break

if p > 0:
    print('NAO')
else:
    print('SIM')
    
