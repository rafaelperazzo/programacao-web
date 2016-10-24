# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
c=int(input('digite o valor de c:'))

while a>0 and b>0 and c>0 and a<=c and b<=c:
    qa=c/a
    qb=c/b
    if c%a==0 and c%b==0:
        c=qa+qb
        print(qa)
        print(qb)
    else:
        print('N')





