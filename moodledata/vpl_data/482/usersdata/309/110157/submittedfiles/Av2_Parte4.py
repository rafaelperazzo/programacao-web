# -*- coding: utf-8 -*-

mt=[]
lin=int(input("Digite a quantidade de linhas da matriz:"))
colu=int(input("Digite a quantidade de colunas da matriz:"))

for i in range (lin-1,-1,-1):
    lista=[]
    for j in range (colu-1,-1,-1):
        print(j)
        lista[j]=int(input("Digite um elemento para sua matriz:"))
    mt[i]=lista

print(mt)
