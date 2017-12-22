# -*- coding: utf-8 -*-
m = int(input('Digite o número de linhas: '))
n = int(input('Digite o número de colunas: '))
matriz = []
for i in range(0,m,1):
    linha = []
    for j in range(0,n,1):
        linha.append(int(input('Digite um elemento da matriz: ')))
    matriz.append(linha)
cont = 0
for i in range(0,n,1):
    cont += matriz[i]
print(cont1)    
    
