# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Digite o valor de a: '))
b=int(input('Digite o valor de b: '))
c=int(input('Digite o valor de uma cédula: '))
if b>c:
    qb=a//b
    qc=(a%b)/c
    if (a%b)%c!=0:
        print('N')
    else:
        print(qb)
        print(qc)
elif c>b:
    qc=a//c
    qb=(a%c)/b
    if (a%c)%b!=0:
        print('N')
    else:
        print(qb)
        print(qc)
else:
    qc=a//c
    qb=0
    if a%c!=0:
        print('N')
    else:
        print(qb)
        print(qc)