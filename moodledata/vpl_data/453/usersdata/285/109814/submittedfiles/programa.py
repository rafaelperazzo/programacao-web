# -*- coding: utf-8 -*-
#Criando Tabuleiro
n= int(input("digite a ordem do tabuleiro: "))
tabuleiro=[]
for i in range(0,n,1):
    tabuleiro_linha=[]
    for j in range(0,n,1):
        tabuleiro_linha.append(int(input("digite o valor (%d,%d): " %(i+1,i+1))))
#somando as linhas
soma_linha=[]
for i in range(0,n,1):
    cont=0
    for j in range(0,n,1):
        cont=cont+tabuleiro[i][j]
    soma_linha.append(cont)
#somando as colunas
soma_coluna=[]
for j in range(0,n,1):
    cont2=0
    for i in range(0,n,1):
        cont2=cont2+tabuleiro[i][j]
    soma_coluna.append(cont2)
#Tupla aonde a peça está
peça=[]
for i in range(0,n,1):
    for j in range(0,n,1):
        if (soma_linha[i]+soma_coluna[j]-2*tabuleiro[i][j])>peça:
            peça=soma_linha[i]+soma_coluna[j]-2*tabuleiro[i][j]
print(peça)            
        

