# -*- coding: utf-8 -*-
qa=int(input('Digite o número de elementos da primeira lista:'))
qb=int(input('Digite o número de elementos da segunda lista:'))
for la in range(1,qa+1,1):
    x=[la]
for lb in range(1,qb+1,1):
    y=[lb]
def qnil(x,y,qa,qb):
    if qa>qb:
        n=(x-y)
        nei=(qa-n)
    else:
        n=(x-y)
        nei=(qb-n)
print(qnil(2,2,2,2))
    