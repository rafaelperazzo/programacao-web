# -*- coding: utf-8 -*-
#n= float(input('Digite o número de linhas: '))
#lista= []
#for i in range (0,n,1):
   # for j in range (0,n,1):
        #lista[i][j]= int(input('Digite o elemento da linha%d da coluna%d: ' %((j+1),(i+1))))
def cria_matriz(m,n,valor_inicial):
    matriz=[]
    for in range(m):
        linha=[]
        for j in range(n):
            linha.append(valor_inicial)
        matriz.append(linha)
    return matriz
