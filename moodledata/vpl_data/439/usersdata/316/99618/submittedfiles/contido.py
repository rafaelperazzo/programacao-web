# -*- coding: utf-8 -*-
qa=int(input('Digite o número de elementos da primeira lista:'))
qb=int(input('Digite o número de elementos da segunda lista:'))
for la in range(1,qa+1,1):
    x=[la]
    print(la)
for lb in range(1,qb+1,1):
    y=[lb]
    print(lb)
print(la-lb)