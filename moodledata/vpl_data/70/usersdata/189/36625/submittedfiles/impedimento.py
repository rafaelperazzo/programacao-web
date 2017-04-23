# -*- coding: utf-8 -*-
import math
r=int(input('digite o valor de r:'))
l=int(input('digite o valor de l:'))
d=int(input('digite o valor de d:'))
x=0
y=50
z=100
if x<y<r>z and x<l<r<z and y<r<d<z:
    print('N')
elif x<y<r>z and x<l<r<z and x<y<r>d<z:
    print('S')