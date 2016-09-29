# -*- coding: utf-8 -*-
from __future__ import division
a=input(' digite o valor a:')
b=input(' digite o valor de b: ')
c=input(' digite o valor de c: ') 
if a>b and b>c:
    print(a)
elif b>a and a>c:
    print(b)
else:
    print(c)