# -*- coding: utf-8 -*-
N = int(input('Digite a dimensão do tabuleiro do quadrado: '))
while n < 3:
    N = int(input('Digite a dimensão do tabuleiro do quadrado: '))
matriz = []
peso_max = 0
soma_linha = 0
soma_coluna = 0
for i in range (0,N,1):
    linha = []
    for j in range (0,N,1):
        linha.append(int(input('Digite um valor para o tabuleiro: ')))
    matriz.append(linha)
