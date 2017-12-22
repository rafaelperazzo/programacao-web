# -*- coding: utf-8 -*-
N= int(input('Digite a ordem da matriz Tabuleiro: '))
while (N<3):
    N= int(input('Digite a ordem da matriz Tabuleiro: '))
tabuleiro= []
for i in range (0,N,1):
    linha=[]
    for j in range (0,N,1):
        linha_l.append(int(input('Digite os elementos da linha %d: ' %(i+1))))
    tabuleiro.append(linha)
#SOMA OS ELEMENTOS DAS LINHAS
linha_l=[]
for i in range (0,N,1):
    soma_l=0
    for j in range(0,N,1):
        soma_l+=tabuleiro[i][j]
    linha.append(soma_l)
#SOMA OS ELEMENTOS DAS COLUNAS
linha_c=[]
for j in range (0,N,1):
    soma_c=0
    for i in range (0,N,1):
        soma_c+=tabuleiro[i][j]
    linha_c.append(soma_c)
maior=0
for i in range (0,n,1):
    for j in range (0,n,1):
        if (linha_l[i]+linha_c[j]-2*tabuleiro[i][j]>maior:
            maior=(linha_l[i]+linha_c[j]-2*tabuleiro[i][j])
print(maior)
    
