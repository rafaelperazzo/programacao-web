# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('Digite o valor do primeiro número:')
b=input('Digite o valor do segundo número:')
c=input('Digite o valor do terceiro número:')
d=input('Digite o valor do quarto número:')
if a>b:
    if c>b and c>d:
        print('N')
    elif d>c:
        print('N')
    elif a==c or a==d:
        print('N')
    else:
        print('N')
elif b>a and b>c:
    if d>c:
        print('N')
    elif b==d:
        print('N')
    else:
        print('S')
elif c>b and c>d:
    print('S')
elif d>c:
    if a==b or a==c or b==c:
        print('N')
    else:
        print('S')
elif a==b or a==c or a==d:
    print('N')