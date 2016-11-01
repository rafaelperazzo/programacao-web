# -*- coding: utf-8 -*-
from __future__ import division

#entrada
a=input('digite o valor de a:')
b=input('digite o valor de b:')
c=input('digite o valor de c:')
#processamento 
qa=c//a

qb=(c-qa*a)//b
#saida
if c==(qa*a+qb*b):
    print(qa)
    print(qb)
else:
    print('N')
