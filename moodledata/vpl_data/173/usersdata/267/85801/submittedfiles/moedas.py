# -*- coding: utf-8 -*-
a=int(input('Moeda a: '))
b=int(input('Moeda b: '))
c=int(input('Cédula: '))
qa=0
qb=0
while (a*qa+b*qb<c):
    qa=qa+1
    while (a*qa+b*qb<c):
        qb=qb+1
print qa
print qb