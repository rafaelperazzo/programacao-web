# -*- coding: utf-8 -*-
from __future__ import division

a=int(input('de po valor de a: '))
b=int(input('de po valor de b: '))
c=int(input('de po valor de c: '))

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
    print ('N')