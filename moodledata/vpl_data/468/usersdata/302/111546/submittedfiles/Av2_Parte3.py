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
    media = 0
    media = sum(matriz[i])/len(matriz[i])
    print('%.2f'%media)
    desvio = 0
    for j in range(n):
        desvio = (((matriz[i][j]-media)**2)) + desvio
    desvio = ((desvio)/(n-1))**(1/2)
    print('%.2f'%desvio)
