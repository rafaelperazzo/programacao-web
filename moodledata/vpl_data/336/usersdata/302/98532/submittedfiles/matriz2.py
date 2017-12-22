# -*- coding: utf-8 -*-
n = int(input('Digite a dimensão da matriz: '))
matriz = []
for i in range(n):
    for i in range(n):
        linha = []
        linha.append(int(input('Digite a linha: ')))
        linha.append(int(input('Digite a linha: ')))
        matriz.append(linha)
print(matriz)
print(matriz[0])
print(sum(matriz[0]))
print(sum(matriz[1]))
s=0
for i in range(n-1):
    if sum(matriz[i]) == sum(matriz[i+1]):
        s=s+1
    if s == n-1:
        print('S')
            
    

 
        
