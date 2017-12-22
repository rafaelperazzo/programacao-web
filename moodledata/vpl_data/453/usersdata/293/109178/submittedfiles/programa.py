# -*- coding: utf-8 -*-
n=int(input("Digite a ordem da matriz: "))
tabuleiro=[]
for i in range(0,n,1):
    tabuleiro_linha=[]
    for j in range(0,n,1):
        tabuleiro_linha.append(int(input("Digite o valor de (%d,%d): "%(i+1,j+1))))
    tabuleiro.append(tabuleiro_linha)

