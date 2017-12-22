# -*- coding: utf-8 -*-
m=int(input('digite a quantidade de listas: '))
n=int(input('digite a quantidade de valores das listas'))
termo1=(1/(n-1))
matriz=[]
for i in range(m):
    lista=[]
    for j in range(n):
        lista.append(float(input('digite os valores: ')))
    matriz.append(lista)
print(matriz)
for i in range (m):
    media=sum(matriz[i])/n
    print(media)
    
    
