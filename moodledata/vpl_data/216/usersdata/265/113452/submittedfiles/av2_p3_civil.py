# -*- coding: utf-8 -*-
n = int(input('digite o tabuleiro: '))
tabuleiro=[]
for i in range(0,n,1):
    linha_tabuleiro=[]
    for j in range(0,n,1):
        linha_tabuleiro.append(int(input('digite o elemento: ')))

linha_soma=[]
for i in range(0,n,1):
    cont=0
    for j in range(0,n,1):
        cont=cont+tabuleiro[i][j]
    linha_soma.append(cont)
    
coluna_soma=[]
for j in range(0,n,1):
    cont2=0
    for i in range(0,n,1):
        cont2=cont2+tabuleiro[i][j]
    coluna_soma.append(cont2)

peça=[]
for i in range(0,n,1):
    if (linha_soma[i]+coluna_soma[j]-2*tabuleiro[i][j])>peça:
        peça=linha_soma[i]+coluna_soma[j]-2*tabuleiro[i][j]

print(peça)

