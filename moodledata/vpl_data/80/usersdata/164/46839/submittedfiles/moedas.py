# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Digite a: '))
b=int(input('Digite b: '))
c=int(input('Digite c: '))
cont=0
while (c//a>0) and (c//b>0):
    if (c>0):
        qa=c//a
        c=c%a
        qb=c//b
        c=c%b
        cont=cont+1
    if (c>0):
        qb=c//b
        c=c%b
        qa=c//a
        c=c%a
        cont=cont+1
if (cont>0):
    print(qa)
    print(qb)
else:
    print('N')