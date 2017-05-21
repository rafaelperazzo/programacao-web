# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Digite a: '))
b=int(input('Digite b: '))
c=int(input('Digite c: '))
cont=0
if (c%a==0) and (c%b==0):
    while (c>0):
        qa=c//a
        c=c%a
        qb=c//b
        c=c%b
        cont=cont+1
if (cont>0):
    print(qa)
    print(qb)
else:
    print('N') 