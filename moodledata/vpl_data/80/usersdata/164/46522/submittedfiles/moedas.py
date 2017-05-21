# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Digite a: '))
b=int(input('Digite b: '))
c=int(input('Digite c: '))
qa=1
qb=1
while (a<1000):
        qa=c//a
        c=c%a    
        qb=c//b
print(qa)
print(qb)