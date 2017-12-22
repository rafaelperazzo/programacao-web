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
somal=0
somac=0
for j in range (0,N,1):
    somal+=tabuleiro[i][j]
for i in range (0,N,1):
    somac+=tabuleiro[i][j]
soma=0
for i in range (0,N,1):
    for j in range(0,N,1):
        soma+=(somal+somac)-tabuleiro[i][j]
    print(soma)

