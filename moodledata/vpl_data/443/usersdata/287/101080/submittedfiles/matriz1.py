# -*- coding: utf-8 -*-
n=int(input("digite o numero de linhas: "))
m=int(input("digite o numero de colunas: "))
matriz=[]
for i in range (0,n,1):
    for j in range (0,m,1):
        matriz.append(int(input("digite o valor do %d da %d: " )))
        
nova_matriz=[]
for i in range (len(matriz)):
    for j in range(len(matriz[0][0])):
        nova_matriz[len(matriz)-(i+1)][len(matriz)-(j+1)]=matriz[i][j]
        
print(nova_matriz)
        
    


