# -*- coding: utf-8 -*-
def teste(lista, inicio, fim, incremento):
    total = 0
    for i in (inicio, fim, incremento):
        if lista[i]>lista[i-incremento]:
            total += 1 
            print('Entrou')
        else:
            print('Não entrou')
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
print(matriz)
for j in range(1):
    if teste(matriz[j], 1, n, 1):
        print('S')
    else:
        print('N')
    if teste(matriz[j], n-2, -1, -1):
        print('S')
    else:
        print('N')
