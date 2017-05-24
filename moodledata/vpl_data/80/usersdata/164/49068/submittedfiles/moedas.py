# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Digite a: '))
b=int(input('Digite b: '))
c=int(input('Digite c: '))
qa=0
qb=0
qaa=qa
while ((qa*a)<c):
    qa=qa+1
if ((qa*a)>c):
    qa=qa-1
while (c%qaa!=qb*b) and (c*qaa"!=0):
    if (c%qaa<qb*b):
        qaa=qaa+1
    elif (c%qaa>=qb*b):
        qb=qb+1
if (qaa*a+qb*b==c):
    print(qaa)
    print(qb)
else:
    print('N')