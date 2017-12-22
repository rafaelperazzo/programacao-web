# -*- coding: utf-8 -*-
import numpy as np
N = int(input("Digite a dimensão do tabuleiro quadrado: "))
while N<3:
    N = int(input("Digite a dimensão do tabuleiro quadrado: "))
tabuleiro = []
for i in range (0,N):
    linha = []
    for j in range (0,N):
        linha.append(int(input("Digite um valor para o tabuleiro: ")))
    tabuleiro.append(linha)
tabuleiro_transp = np.empty([N,N])
for j in range (0,N):
    for i in range (0,N):
        tabuleiro_transp[j][i] = tabuleiro[i][j]
soma_total = sum(tabuleiro[0]) + sum(tabuleiro_transp[0]) - 2*(tabuleiro[0][0])
for i in range (0.N):
    if soma_total = sum(tabuleiro[i]) + sum(tabuleiro_transp[j]) - 2*(tabuleiro[i][j]):
        soma_total = soma_total
    else:
        soma_total = sum(tabuleiro[i]) + sum(tabuleiro_transp[j]) - 2*(tabuleiro[i][j])
print(int(soma_total))
