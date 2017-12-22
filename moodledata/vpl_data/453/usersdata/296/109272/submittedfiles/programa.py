# -*- coding: utf-8 -*-
n = int(input('Digite a dimensão do quadrado: '))
while n < 3:
    n = int(input('Digite a dimensão do quadrado: '))
matriz = []
for i in range (0,n,1):
    linha = []
    for j in range (0,n,1):
        linha.append(int(input('Digite o valor para a matriz: ')))
    matriz.append(linha)
    
print(matriz)
