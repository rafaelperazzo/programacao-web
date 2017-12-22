# -*- coding: utf-8 -*-
matriz = []
n = int(input("Digite o número de linhas: "))
m = int(input("Digite o número de colunas: "))
for i in range (0,n,1):
    lista = []
    for j in range (0,m,1):
        lista.append(int(input("Digite o elemento da linha%.d e da coluna%.d: " %(i,j))))
    matriz.append(lista)
matrizX = []
for i in range (0,n,1):
    for j in range (0,m,1):
        if matriz[i][j]==1:
            matrizX.append(matriz[i])
print(matrizX)
            
        
    

