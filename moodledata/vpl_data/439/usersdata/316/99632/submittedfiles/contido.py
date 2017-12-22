# -*- coding: utf-8 -*-
qa=input('Digite o número de elementos da primeira lista:')
qb=input('Digite o número de elementos da segunda lista:')
for la in range(1,qa+1,1):
    x=[la]
for lb in range(1,qb+1,1):
    y=[lb]
def qnil(x,y,qa,qb):
    if qa>qb:
        nei=(qa-x+y)
        return
    else:
        nei=(qb-x+y)
        return
print(qnil(x,y,qa,qb))

    