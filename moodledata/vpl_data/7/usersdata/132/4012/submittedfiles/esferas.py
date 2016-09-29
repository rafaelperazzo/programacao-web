# -*- coding: utf-8 -*-
from __future__ import division
a=input(' digite o valor da esfera 1:')
b=input(' digite o valor da esfera 2:')
c=input(' digite o valor da esfera 3:')
d=input(' digite o valor da esfera 4:')
if a==b+c+d and b+c==d and b==c:
    print('s')
else:
    print('n')