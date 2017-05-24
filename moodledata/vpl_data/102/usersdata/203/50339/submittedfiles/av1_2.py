# -*- coding: utf-8 -*-
import math
a=int(input('digite a: '))
b=int(input('digite b: '))
c=int(input('digite c: '))
d=int(input('digite d: '))
if a==c and b!=d:
    print('V')
elif b==d and a!=c:
    print('V')
else:
    print('F')