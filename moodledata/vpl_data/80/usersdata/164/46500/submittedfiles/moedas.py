# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Digite a: '))
b=int(input('Digite b: '))
c=int(input('Digite c: '))
qa=0
qb=0
while (a>0 and b>0):
    if (a>0):
        a=a%c
        qa=qa+1
    if (b>0):
        b=b%c
        qb=qb+1
print(qa)
print(qb)