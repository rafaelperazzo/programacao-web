# -*- coding: utf-8 -*-

matriz = []
matriz2 = [[]]

for i in range (1, 50):
    matriz.append(i)
    matriz2[0].append(i)

for i in range (0, 100):
    try:
        print(id(matriz[i]))
        print(id(matriz[0][i]))
    except:
        print('Fim')
        break
print('Acabou')