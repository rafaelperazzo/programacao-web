# -*- coding: utf-8 -*-
import numpy as np
N = int(input("Digite a dimensão do tabuleiro quadrado: "))
while N<3:
    N = int(input("Digite a dimensão do tabuleiro quadrado: "))
tabuleiro = []
for i in range (0,N,1):
    linha = []
    for j in range (0,N,1):
        linha.append(int(input("Digite um valor para o tabuleiro: ")))
    tabuleiro.append(linha)
tabuleiro_transp = np.empty ([N,N])
for j in range (0,N,1):
    for i in range (0,N,1):
        tabuleiro_transp[j][i] = tabuleiro[i][j]
soma_total = sum(tabuleiro[0]) + sum(tabueliro_transp[0]) - 2*(tabuleiro[0][0])
for i in range (0.N,1):
    if soma_total = sum(tabuleiro[i]) + sum(tabueliro_transp[j]) - 2*(tabuleiro[i][j]):
        soma_total = soma_total
    else:
        soma_total = sum(tabuleiro[i]) + sum(tabueliro_transp[j]) - 2*(tabuleiro[i][j])
print(int(soma_total))
