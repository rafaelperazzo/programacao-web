# -*- coding: utf-8 -*-
matriz=[]
m=int(input("digite o valor de linhas da matriz: "))
n=int(input("digite o valor de colunas da: "))
for i in range(0,m,1):
    lista=[]
    for j in range(0,n,1):
        linha.append(int(input("digite o valor do %dº elemento da %d lista: " %(j+1),(i+1))))
    matriz.append(linha)
for linha in matriz:
    linha.reverse()
matriz.reverse()
print(matriz)
        
