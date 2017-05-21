# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Valor de a:'))
b=int(input('Valor de b:'))
c=int(input('Valor de c:'))
qa=c//a
resto=c%a
if resto>0:
    qb=c/resto
    if c%resto==0:
        print(qa)
        print(qb)
    else:
        print('N')    
else:
    qb=0
    print(qa)
    print(qb)

