# -*- coding: utf-8 -*-
import math
r=int(input('digite o valor de r:'))
l=int(input('digite o valor de l:'))
d=int(input('digite o valor de d:'))

if r>50 and l>r and r<d:
    print('N')
if r>50 and l>r and r>d:
    print('S')