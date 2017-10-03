# -*- coding: utf-8 -*-

n = int(input('competidores: '))
p = float(input('nota minima: '))

T = [0]*n
J = [0]*n

for i in range (n):
    b = i+1
    T[i] = int(input('Nota 1: '))
    J[i] = int(input('Nota 2: '))
    if T[i]+J[i] >= p:
        print('passou')
    else:
        print('nao passo')














