# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Digite o valor de moeda a: '))
b=int(input('Digite o valor de moeda b: '))
c=int(input('Digite o valor de cédula c: '))
qa=c//a
qb=(c%a)//b
qd=(c%a)%b
if qa==0 or qa!=0 and qd==0:
    print(qa)
    print(qb)
else:
    print('N')
