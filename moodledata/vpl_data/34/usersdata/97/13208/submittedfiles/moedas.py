# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
c=int(input('digite o valor de c:'))

qa=c/a
qb=c/b
while a>0 and b>0 and c>0:
    if c%a==0 and c%b==0:
        qa=c/a
        qb=c/b

        print(qa)
        print(qb)
    else:
        print('N')





