# -*- coding: utf-8 -*-
n=int(input("Digite a ordem da matriz: "))
while(True):
    if n<2:
        n=int(input("Digite a ordem da matriz: "))
    else:
        break
###MATRIZ nxn###
matriz=[]
for i in range(0,n,1):
    matriz_linha=[]
    for j in range(0,n,1):
        matriz_linha.append(int(input("Digite o elemento (%d,%d): "%(i+1,j+1))))
    matriz.append(matriz_linha)
    
###SOMA DAS LINHAS###
soma_linhas=0
for i in range(0,n,1):
    soma_linhas= sum(matriz[i])+ soma_linhas
###SOMA DAS COLUNAS###
soma_colunas=0
for j in range(0,n,1):
    for i in range(0,n,1):
        soma_colunas= matriz[i][j]+ soma_colunas
print(matriz)
print(soma_colunas)

###SOMA DAS DIAGONAIS PRINCIPAIS###
soma_dp=0
for i in range(0,n,1):
    for j in range(0,n,1):
        if i==j:
            soma_dp=matriz[i][j]+ soma_dp
###SOMA DAS DIAGONAIS SECUNDÁRIAS###
soma_ds=0
for i in range(0,n,1):
    for j in range(0,n,1):
        if i+j==n-1:
            soma_ds=matriz[i][j] + soma_ds

if soma_dp==soma_ds==(soma_colunas/n)==(soma_linhas/n):
    print("S")
else:
    print("N")
    