# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Valor de a:'))
b=int(input('Valor de b:'))
c=int(input('Valor de c:'))
qa=c//a
resto=c%a
qb=resto//b
if resto%b==0:
    print(qa)
    print(qb)
else:
    print('N')

