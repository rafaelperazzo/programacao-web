# -*- coding: utf-8 -*-
num  = int(input('Número de competidores: '))
nm = float(input('Nota mínima: '))

i = 1
total = 0

while i<=num:
    n1 = float(input('Candidato %d nota 1: ' % i))
    n2 = float(input('Candidato %d nota 2: ' % i))
    if ((n1+n2)>= nm):
        total += 1
    i += 1
print('%d' % total)