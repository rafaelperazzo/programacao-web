# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Digite a: '))
b=int(input('Digite b: '))
c=int(input('Digite c: '))
qa=0
qb=0
while (a<1000):
    if (a>b):
        qa=c//a
        c=c%a
        qb=c//b
    else:
        qb=c//b
        c=c%b
        qa=c//a
print(qa)
print(qb)