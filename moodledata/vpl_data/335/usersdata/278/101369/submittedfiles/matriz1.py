# -*- coding: utf-8 -*-
matriz = []
n = int(input("Digite o número de linhas: "))
m = int(input("Digite o número de colunas: "))
for i in range (0,n,1):
    lista = []
    for j in range (0,m,1):
        lista.append(int(input("Digite o elemento da linha%.d e da coluna%.d: " %(i,j))))
    matriz.append(lista)
print(matriz)
matrizX = []
listaX = []
for i in range (0,n,1):
    for j in range (0,m,1):
        if matriz[i][j]==1:
            x = i
            break
for i1 in range (n-1,-1,-1):
    for j in range (0,m,1):
        if matriz[i1][j]==1:
            x1 = i1
            break
for j in range (0,m,1):
    for i in range (0,n,1):
        if matriz[i][j]==1:
            y = j
            break
for j1 in range (m-1,-1,-1):
    for i in range (0,n,1):
        if matriz[i][j1]==1:
            y1 = j1
            break
print(x)
print(x1)
print(y)
print(y1)
for i in range (y1,y,1):
    for j in range (x1,x,1):
        listaX.append(matriz[i][j])
    matrizX.append(listaX)
print(matrizX)


            
        
    

