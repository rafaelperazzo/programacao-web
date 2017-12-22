# -*- coding: utf-8 -*-
n=int(input('digite a dimensao do tabuleiro: '))
tabuleiro=[]
for i in range(0,n,1):
    colunas=[]
    for j in range(0,n,1):
        colunas.append(float(input('digite o elemento da linhas%d, coluna%d :' %((j+1),(i+1)))))
    tabuleiro.append(colunas)
    
