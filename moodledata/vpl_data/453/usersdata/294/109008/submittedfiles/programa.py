# -*- coding: utf-8 -*-
N= int(input('Digite a ordem da matriz Tabuleiro: '))
while (N<3):
    N= int(input('Digite a ordem da matriz Tabuleiro: '))
    if N>=3:
        break
tabuleiro= []
for i in range (0,N,1):
    linha=[]
    for j in range (0,N,1):
        linha.append(int(input('Digite o elemendo %d da linha: ' %(i+1))))
    tabuleiro.append(linha)
print(tabuleiro)
soma=0
for i in range (0,N,1):
    for j in range (0,N,1):
        soma+=tabuleiro[i][j]

