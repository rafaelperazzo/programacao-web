# -*- coding: utf-8 -*-
i=1
qa=input('Digite o número de elementos da primeira lista:')
while i<=qa:
    x=int(input('digite um numero:'))
    i=i+1
i=1
qb=input('Digite o número de elementos da segunda lista:')
while i<=qb:
    y=int(input('digite um numero:'))
    i=i+1
def fim(qa,x,qb,y):
    if qa>=qb:
        w=qa-x+y
    else:
        w=qb-x+y
    return w
print(w)



    