# -*- coding: utf-8 -*-
import math

a=float(input(' Digite o valor a'))
b=float(input(' Digite o valor b'))
c=float(input(' Digite o valor c'))
d=float(input(' Digite o valor d'))

if (a>b) and (a>c) and (a>d):
    print('S')
elif (b>c) and (b>a) and (b>d):
    print('S')
elif (c>a) and (c>b) and (c>d):
    print('S')
elif (d>a) and (d>b) and (d>c):
    print ('S')
else:
    print('N')