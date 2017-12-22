# -*- coding: utf-8 -*-
m=int(input("Digite a quantidade de listas: "))
n=int(input("Digite a quantidade de elementos para a sua lista: "))
matriz=[]
for i in range(0,m,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input("Digite o elemento da sua lista: ")))
    matriz.append(linha)

media=[]
for i in range(0,m,1):
    media.append(sum(matriz[i])/n)

