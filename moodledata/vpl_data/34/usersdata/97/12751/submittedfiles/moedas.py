# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
c=int(input('digite o valor de c:'))

while a>0 and b>0 and c>0 and a<=c and b<=c:
    if c%a==0 and c%b==0:
        qa=c/a
        qb=c/b
        c=qa+qb
        print(qa)
        print(qb)
    elif c%a!=0 or c%b!=0:
        print('N')





