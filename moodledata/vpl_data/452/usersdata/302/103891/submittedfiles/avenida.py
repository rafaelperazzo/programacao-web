# -*- coding: utf-8 -*-
m = int(input('Digite o número de linhas: '))
n = int(input('DIgite o número de colunas: '))
matriz = []
for i in range(m):
    linha = []
    for j in range(n):
        linha.append(float(input('Digite o elemento %d de %d: ' %((j+1),(i+1)))))
    matriz.append(linha)
print(matriz)
#linhas
a = 0
b = 0
c = 0
for i in range(m-1):
    if sum(matriz[i]) > sum(matriz[i+1]):
        a = len
    else:
        b = b+1
        
        
        
