# -*- coding: utf-8 -*-
n=int(input("Digite a ordem da matriz: "))
matriz=[]
for i in range (0,n,1):
    linha=[]
    for j in range (0,n,1):
        linha.append(int(input("Digite um numero da matriz: ")))
    matriz.append (linha)
    
soma_linha=[]
for i in range (0,n,1):
   soma_linha.append(sum(matriz[i]))
   
soma_coluna=[]
for j in range

