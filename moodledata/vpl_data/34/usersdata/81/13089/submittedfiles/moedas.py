# -*- coding: utf-8 -*-
from __future__ import division

a=int(input('Digite o valor da primeira moeda:'))
b=int(input('Digite o valor da segunda moeda:'))
c=int(input('Digite o valor da cédula:'))
qa=0
qb=0
cont=0

while qa<=c//a:
    qb=(c-qa*a)//b
    if qa*a+qb*b==c:
        cont+=1
        break
    else:
        qa+=1
if cont>0:
    print qa
    print qb
else:
    print('N')