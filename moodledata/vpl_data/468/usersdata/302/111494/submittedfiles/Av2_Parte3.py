# -*- coding: utf-8 -*-

m = int(input('Digite a quantidade de listas: '))
n = int(input('Digite o número de elementos das listas: '))
matriz = []
for i in range(m):
    lista = []
    for j in range(n):
        lista.append(float(input('Digite o elemento %d da lista %d:' %((j+1),(i+1)))))
    matriz.append(lista)
for i in range(m):
    media = sum(matriz[i])/len(matriz[i])
    print(media)
    for j in range(n):
        desvio = (((matriz[i][j]-media)**2)/n-1)**(1/2)
    print(desvio)
