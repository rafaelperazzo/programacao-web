# -*- coding: utf-8 -*-
import math
a=int(input('Digite o valor do número a:'))
b=int(input('Digite o valor do número b:'))
c=int(input('Digite o valor do número c:'))
d=int(input('Digite o valor do número d:'))
if a>b and b>c and c>d:
    print('S')
elif b>a and b>c and c>d:
    print('S')
elif c>b and c>d and b>a:
    print('S')
elif d>c and b>a and c>b:
    print('S')
else:
    print('N')