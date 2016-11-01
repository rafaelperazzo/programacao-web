# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite um valor:'))
b=int(input('digite um valor:'))
c=int(input('digite um valor:'))

d=c//a
e=c//b
f=c%a
g=c%b

if c%a!=0 and c%b==0 or c%b!=0:
    qa=d
    print(qa)
    qb=f//b
    print(qb)
    
elif c%b!=0 and c%a!=0 or c%a==0:
    qa=g//a
    print(qa)
    qb=e
    print(qb)

elif f//b!=0 or g//a!=0:
    print('N')