# -*- coding: utf-8 -*-
m=int(input("Digite a quantidade de listas: "))
n=int(input("Digite a quantidade de elementos de cada lista:"))
matriz=[]
for i in range(0,m,1):
    l=[]
    for j in range(0,n,1):
        l.append(int(input("Digite o elemento")))
    matriz.append(l)
media=0
for i in range(0,m,1):
    for j in range(0,n,1):
        media=media+media[i][j]
    media=media/(len(matriz[0])
print(media)    


