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
            break
    return i
for i1 i range (n-11,-1,-1):
    for j in range (0,m,1):
        if matriz[i1][j]==1:
            break
    return i1
for j in range (0,m,1):
    for i in range (0,n,1):
        if matrizX[i][j]==1:
            break
    return j
for j1 in range (m-1,-1,-1):
    for i in range (0,n,1):
        if matrizX[i][j1]==1:
            break
    return j1
for a in range (i,i1+1,1):
    for b in range (j,j1+1,1):
        matrizX.append(matriz[a][b])
print(matrizX)


            
        
    

