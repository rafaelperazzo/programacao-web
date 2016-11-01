# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite A:'))
b=int(input('digite B:'))
c=int(input('digite C:'))
cont=0
for i in range (0,c-1,a):
    if (c-i)%b==0:
        qa=i//a
        qb=(c-i)//b
        cont=1
if cont==0:
    print('N')
if cont==1:
    print(qa)
    print(qb)