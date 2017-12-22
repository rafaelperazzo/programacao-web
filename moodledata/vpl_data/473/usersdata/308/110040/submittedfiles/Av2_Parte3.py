# -*- coding: utf-8 -*-
def teste(lista, inicio, fim, incremento):
    total = 0
    for i in (inicio, fim, incremento):
        if lista[i]>lista[i-incremento]:
            total += 1 
            print('Entrou')
    if total == (len(lista)-1):
        return True
    else:
        return False

n = int(input('Informe o valor de N: '))
matriz = []
for i in range(1):
    matriz.append([])
    for j in range(n):
        matriz[i].append(int(input('Informe o valor %d da lista %d: ' % (j,i))))

for i in range(3):
    if teste(matriz[i], 1, 1, 1):
        print('S')
    else:
        print('N')
    if teste(matriz[i], len(matriz[i])-2, -1, -1):
        print('S')
    else:
        print('N')
