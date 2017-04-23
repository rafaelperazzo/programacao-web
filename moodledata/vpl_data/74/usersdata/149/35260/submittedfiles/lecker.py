# -*- coding: utf-8 -*-
import math
a=int(input('digitite o valor 1:'))
b=int(input('digitite o valor 2:'))
c=int(input('digitite o valor 3:'))
d=int(input('digitite o valor 4:'))
if b>a and b>c or c>b and c>d:
    print('S')
if c>a and c>b or b>c and b>d:
    print('S')
if b>d and b>c or c>b and c>a:
    print('S')