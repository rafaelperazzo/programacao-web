# -*- coding: utf-8 -*-
def teste(lista, inicio, fim, incremento):
    total = 0
    for i in (inicio, fim, incremento):
        if lista[i]>lista[i-incremento]:
            total += + 1 
    if total == (len(lista)-1):
        return True
    else:
        return False

n = int(input('Informe o valor de N: '))
matriz = []
for i in range(3):
    matriz.append([])
    for j in range(n):
        matriz[i].append(int(input('Informe o valor %d da lista %d: ' % (j,i))))

for i in range(3):
    for incremento in [1, -1]:
        if teste(matriz[i], 1, 1, incremento):
            print('S')
        else:
            print('N')
        #print(teste(matriz[i], len(matriz[i])-2, -1, -1))
