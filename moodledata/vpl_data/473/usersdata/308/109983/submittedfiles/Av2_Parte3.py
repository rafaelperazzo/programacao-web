# -*- coding: utf-8 -*-
def teste(lista, incremento, inicio):
    for i in (inicio, len(lista), incremento):
        if lista[i]>lista[i-incremento]:
            return 'S'
    return 'N'

n = int(input('Informe o valor de N: '))
matriz = []
for i in range(3):
    matriz.append([])
    for j in range(n):
        matriz[i].append(int(input('Informe o valor %d da lista %d: ' % (j,i))))

for i in range(3):
        print(teste(matriz[i], 1, 1))
        print(teste(matriz[i], 1, 1))
