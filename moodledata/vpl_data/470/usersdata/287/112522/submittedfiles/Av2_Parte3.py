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
    desvpad1=(1/(n-1))
    media=sum(matriz[i])/n
    print(media)
    for j in range(n+2):
        for k in range(m+2):
            desvpad2=((matriz[j][k]-media)**2)
            desvpad2+=desvpad2
    desvpad=((desvpad1*desvpad2)**0.5)
    print(desvpad)
    
    
