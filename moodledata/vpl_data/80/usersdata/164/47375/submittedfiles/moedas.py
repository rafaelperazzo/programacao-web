# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Digite a: '))
b=int(input('Digite b: '))
c=int(input('Digite c: '))
cont=0
while (c>0):
    qa=c//a
    c=c%a
    qb=c//b
    c=c%b
    a1=(qa*a)
    b1=(qb*b)
    soma=a1+b1
    if (soma==c):
        cont=cont+1
if (cont>0):
    print(qa)
    print(qb)
else:
    print('N') 