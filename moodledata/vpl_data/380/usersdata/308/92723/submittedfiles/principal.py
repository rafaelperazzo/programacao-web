# -*- coding: utf-8 -*-

matriz = []

for i in range (1, 50)
    matriz.append(i)

for i in range (0, 100):
    try:
        print(id(matriz[i]))
    except:
        print('Fim')
        break
print('Acabou')