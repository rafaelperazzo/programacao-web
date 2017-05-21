# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite o valor de a :'))
b=int(input('digite o valor de b:'))
c=int(input('digite o valor de c :'))
cont=0
while c>0:
    qa=c//a
    c=c%a
    qb=c//b
    cont=cont+1
if (cont>0):
    print(qa)
    print(qb)
elif cont<=0:
    print('N')