# -*- coding: utf-8 -*-
m=int(input('digite a quantidade de listas: '))
n=int(input('digite a quantidade de valores das listas'))

matriz=[]
for i in range(m):
    lista=[]
    for j in range(n):
        lista.append(float(input('digite os valores: ')))
    matriz.append(lista)
print(matriz)
for i in range (m):
    termo1=(1/(n-1))
    media=sum(matriz[i])/n
    print(media)
    for j in range(n-1):
        for k in range(m-1):
            desvpad=((termo1*((matriz[n][m]-media)**2))**0.5)
            print(desvpad)
    
    
