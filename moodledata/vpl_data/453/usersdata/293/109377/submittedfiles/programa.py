# -*- coding: utf-8 -*-
n=int(input("Digite a ordem da matriz: "))
tabuleiro=[]
for i in range(0,n,1):
    tabuleiro_linha=[]
    for j in range(0,n,1):
        tabuleiro_linha.append(int(input("Digite o valor de (%d,%d): "%(i+1,j+1))))
    tabuleiro.append(tabuleiro_linha)
    
##SOMA DAS LINHAS##
soma_linhas=[]
for i in range(0,n,1):
    soma_linhas.append(sum(tabuleiro[i]))
    
soma_colunas=[]
for j in range(0,n,1):
    cont=0
    for i in range(0,n,1):
        cont=cont+tabuleiro[i][j]
    soma_colunas.append(cont)
peso=0
for i in range(0,n,1):
    for j in range(0,n,1):
        if (soma_linhas[i]+soma_colunas[j]-(2*tabuleiro[i][j]))> peso:
            peso=(soma_linhas[i]+soma_colunas[j]-(2*tabuleiro[i][j]))
print(peso)        