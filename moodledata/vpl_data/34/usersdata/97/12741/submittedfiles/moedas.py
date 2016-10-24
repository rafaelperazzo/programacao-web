# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
c=int(input('digite o valor de c:'))

while a<=c and b<=c:
    qa=c/a
    qb=c/b
    c=qa+qb
    if c%a==0 and c%b==0:
        print(qa)
        print(qb)
    else:
        print('N')





