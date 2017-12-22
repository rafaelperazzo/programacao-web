# -*- coding: utf-8 -*-
N= int(input('Digite a ordem da matriz Tabuleiro: '))
tabuleiro= []
for i in range (0,N,1):
    linha=[]
    for j in range (0,N,1):
        linha.append(int(input('Digite o elemendo %d da linha: ' %(i+1))))
    tabuleiro.append(linha)
print(tabuleiro)
