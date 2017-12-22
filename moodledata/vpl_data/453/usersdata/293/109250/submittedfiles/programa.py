# -*- coding: utf-8 -*-
n=int(input("Digite a ordem da matriz: "))
tabuleiro=[]
for i in range(0,n,1):
    tabuleiro_linha=[]
    for j in range(0,n,1):
        tabuleiro_linha.append(int(input("Digite o valor de (%d,%d): "%(i+1,j+1))))
    tabuleiro.append(tabuleiro_linha)
    
##SOMA DAS LINHAS##
soma_linhas=0
for i in range(0,n,1):
    soma_linhas = soma_linhas + sum(tabuleiro[i])
print(soma_linhas)
##SOMA COLUNAS##
soma_colunas=0
for j in range(0,n,1):
    for i in range(0,n,1):
        soma_colunas= tabuleiro[i][j] + soma_colunas
print(soma_colunas)
