# -*- coding: utf-8 -*-
from __future__ import division

a=input('valor da moeda de a:')
b=input('valor da moeda de b:')
c=input('valor da nota de c:')

a>0 and b>0 and c>0

qa=c//a
qb=(c%a)//b

if qb==0:
    print(qa)
    print(qb)
    
else:
    print('N')