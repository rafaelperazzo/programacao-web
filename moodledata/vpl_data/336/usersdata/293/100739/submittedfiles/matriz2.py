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
soma=0
for i in range(0,n,1):
    soma= sum(matriz[i])+ soma
print(soma)


