# -*- coding: utf-8 -*-
def teste(lista, inicio, fim, incremento):
    total = 0
    for i in range(inicio, fim, incremento):
        if lista[i]>lista[i-incremento]:
            total += 1 
    if total == (len(lista)-1):
        return 'S'
    else:
        return 'N'

n = int(input('Informe o valor de N: '))
matriz = []
for i in range(3):
    matriz.append([])
    for j in range(n):
        matriz[i].append(int(input('Informe o valor %d da lista %d: ' % (j,i))))
for j in range(3):
    print(teste(matriz[j], 1, n, 1))
    print(teste(matriz[j], n-2, -1, -1))