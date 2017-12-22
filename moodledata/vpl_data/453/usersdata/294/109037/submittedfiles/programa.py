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
        linha.append(int(input('Digite os elementos da linha %d: ' %(i+1))))
    tabuleiro.append(linha)
print(tabuleiro)
#SOMA OS ELEMENTOS DAS LINHAS
for i in range (0,N,1):
    soma_l=0
    for j in range(0,N,1):
        soma_l+=tabuleiro[i][j]
    somaTotal_l=soma_l-tabuleiro[i][j]
    print(soma_l)
    print(somaTotal_l)
#SOMA OS ELEMENTOS DAS COLUNAS
for j in range (0,N,1):
    soma_c=0
    for i in range (0,N,1):
        soma_c+=tabuleiro[i][j]
    somaTotal_c=soma_c-tabuleiro[i][j]
    print(soma_c)
    print(somaTotal_c)
    
