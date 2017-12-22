# -*- coding: utf-8 -*-
def primeiralinha(matriz):
    for i in range(0,matriz.shape[0],1):
        for j in range(0,matriz.shape[1],1):
            if matriz[i,j] ==1:
                return(i)
                
def primeiracoluna(matriz):
    for j in range(0,matriz.shape[1],1):
        for i in range(0,matriz.shape[0],1):
            if matriz[i,j] ==1:
                return(j)
                
def ultimacoluna(matriz):
    for j in range(matriz.shape[1] -1,-1,-1):
        for i in range(matriz.shape[0]-1,-1,-1):
            if matriz[i,j]==1:
                return(j)
                
def ultimalinha(matriz):
    for i in range(matriz.shape[0]-1,-1,-1):
        for j in range(matriz.shape[1]-1,-1,-1):
            if matriz[i,j]==1:
                return(i)
                
linhas=int(input("Digite a quantidade de linhas: "))
colunas=int(input("Digite a quantidade de colunas: "))

matriz= np.zeros(linhas,colunas)

for i in range(0,n,1):
    for j in range(0,m,1):
        matriz[i,j]=float(input("Digite os números da matriz(pelas linhas): "))
        

menorlinha= primeiralinha(matriz)
maiorlinha= ultimalinha(matriz)
menorcoluna= primeiracoluna(matriz)
maiorcoluna= ultimacoluna(matriz)

matriz2=matriz[menorlinha:maiorlinha+1,menorcoluna:maiorcoluna+1)

print(matriz2)