# -*- coding: utf-8 -*-


n = int(input('competidores: '))
p = float(input('nota minima: '))

contador=0


T = [0]*n
J = [0]*n

for i in range (n):
    b = i+1
    T[i] = int(input('Nota 1 competidor %d: '%b))
    J[i] = int(input('Nota 2 competidor %d: '%b))
    if (T[i] + J[i]) >= p:
        contador = contador+1


print('%d'%contador)








