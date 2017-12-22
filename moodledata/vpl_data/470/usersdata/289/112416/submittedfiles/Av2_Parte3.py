# -*- coding: utf-8 -*-
m=int(input("Digite a quantidade de listas: "))
n=int(input("Digite a quantidade de elementos de cada lista:"))
matriz=[]
for i in range(0,m,1):
    l=[]
    for j in range(0,n,1):
        l.append(int(input("Digite o elemento")))
    matriz.append(l)
print(matriz)
for i in range(0,m,1):
    soma=0
    for j in range(0,n,1):
        soma+=matriz[i][j]
        media=soma/n
    print(media)
    
    

    
   


