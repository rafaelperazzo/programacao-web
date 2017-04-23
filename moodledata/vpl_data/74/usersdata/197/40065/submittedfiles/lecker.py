# -*- coding: utf-8 -*-
import math
a=int(input('Digite o valor do número a:'))
b=int(input('Digite o valor do número b:'))
c=int(input('Digite o valor do número c:'))
d=int(input('Digite o valor do número d:'))
if a>b:
    if c>b and c>d or d>c:
        print('N')
    else:
        print('S')
elif b>a and b>c:
    if c>b and c>d or d>c:
        print('N')
    else:
        print('S')
elif c>d and c>b:
    if a>b:
        print('N')
    else:
        print('S')
elif d>c:
    if a<b and c<b:
        print('N')
    else:
        print('S')
else:
    print('N')