# -*- coding: utf-8 -*-
import math
w = int(input('Digite o valor de w: '))
x = int(input('Digite o valor de x: '))
y = int(input('Digite o valor de y: '))
z = int(input('Digite o valor de z: '))
if (w>x) and (x>=y) and (y>=z) or (w>x) and (x<=y) and (y==z) :
    print('S')
elif (z>y) and (y>=x) and (x>=w) or (z>y) and (y>=x) and (w==x) :
    print('S')
elif (w<x) and (x>y) and (y>=z) :
    print('S')
elif (y>z) and (y>x) and (x>=w) :
    print('S')
else:
    print('N')