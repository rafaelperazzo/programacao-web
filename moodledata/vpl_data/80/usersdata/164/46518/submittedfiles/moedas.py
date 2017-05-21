# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Digite a: '))
b=int(input('Digite b: '))
c=int(input('Digite c: '))
qa=1
qb=1
while (a<1000):
    if (c%a>=0):
        qa=c//a
    if (c%b>=0):
        qb=c//b
        print(qa)
        print(qb)