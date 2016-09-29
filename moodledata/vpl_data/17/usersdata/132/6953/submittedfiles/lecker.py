# -*- coding: utf-8 -*-
from __future__ import division
import math
a= input(' digite um valor:')
b= input(' digite um valor:')
c= input(' digite um valor:')
d= input(' digite um valor:')
if a<=b<=c<=d:
    print('S')
if a<=b>=c>=d:
    print('S')
if a<=b<=c>=d:
    print('S')
if a>=b>=c>=d:
    print('S')
else:
    print('N')    