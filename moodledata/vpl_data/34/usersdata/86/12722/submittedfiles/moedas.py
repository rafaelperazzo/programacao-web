# -*- coding: utf-8 -*-
from __future__ import division

a = int(input('digite a:'))
b = int(input('digite b:'))
c = int(input('digite c:'))


if (c%a)%b==0:
    qa = c//a
    qb = (c%a)//b
    print(qa)
    print(qb)

elif (c%b)%a==0:
    qb = c//b
    qa = (c%b)//a
    print(qa)
    print(qb)
    
else:
    print('N')
