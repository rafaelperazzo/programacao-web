# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('digite a: '))
b=int(input('digite b: '))
c=int(input('digite c: '))
qa=c//a
d=c%a
qb=d//b
f=c%b
if f!=0 and d!=0:
    print('N')
else:
    print(qa,qb)
    
    