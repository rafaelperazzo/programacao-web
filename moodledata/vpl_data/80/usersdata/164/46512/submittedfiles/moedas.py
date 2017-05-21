# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Digite a: '))
b=int(input('Digite b: '))
c=int(input('Digite c: '))
qa=0
qb=0
while (a<1000):
    if (c%a>0):
        a=c//a
        qa=qa+a
        a=c%a
    if (c%b>0):
        b=c//b
        qb=qb+b
        b=c%b
print(qa)
print(qb)