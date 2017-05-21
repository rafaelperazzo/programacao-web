# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Digite o valor de a: '))
b=int(input('Digite o valor de b: '))
c=int(input('Digite o valor de uma cédula: '))
if b>a:
    qb=c//b
    qa=(c%b)/a
    if (c%b)%a!=0:
        print('N')
    else:
        print(qa)
        print(qb)
elif a>b:
    qa=c//a
    qb=(c%a)/b
    if (c%a)%b!=0:
        print('N')
    else:
        print(qa)
        print(qb)
else:
    qa=c//a
    qb=0
    if c%a!=0:
        print('N')
    else:
        print(qa)
        print(qb)