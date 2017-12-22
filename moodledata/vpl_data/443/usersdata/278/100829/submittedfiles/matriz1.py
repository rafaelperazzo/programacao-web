# -*- coding: utf-8 -*-
m = int(input("Digite a quantidade de linhas: "))
n = int(input("Digite a quantidade de coluas: "))
matriz = []
matrizX = []
for i in range (0,m,1):
    for j in range (0,n,1):
        matriz.append(int(input("Digite o elemento da linha%.d e coluna%.d: " %(i,j))))
for i in range (m-1,-1,-1):
    for j in range (n-1,-1,-1):
        matrizX.append(matriz[i][j])
        

