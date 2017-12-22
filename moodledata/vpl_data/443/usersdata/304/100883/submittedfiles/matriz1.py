# -*- coding: utf-8 -*-

matriz = []
m = int(input('Digite a quantidade de linhas: '))
n = int(input('Digite a quantidade de colunas: '))
for i in range (0,m,1):
    linha = []
    for j in range (0,n,1):
        linha.append(int(input('Digite um elemento: ')))
    matriz.append(linha)

linha = len(matriz)
coluna = len(matriz[0])
i_linha = linha 
i_coluna = coluna
f_linha = 0
f_coluna = 0
for i in range (0,linha,1):
    for j in range (0,coluna,1):
        a = matriz[0][0]
        b = matriz[linha][coluna]
        a = b
        b = a