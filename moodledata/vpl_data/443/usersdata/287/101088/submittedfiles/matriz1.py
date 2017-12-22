# -*- coding: utf-8 -*-
n=int(input("digite o numero de linhas: "))
m=int(input("digite o numero de colunas: "))
matriz=[]
for i in range (0,n,1):
    linha=[]
    for j in range (0,m,1):
        linha.append(int(input("digite o valor do %d da %d: " )))
    matriz.append(linha)
print(matriz)
        
for linha in matriz:
    linha.reverse()
matriz.reverse()
print(matriz)
    


