# -*- coding: utf-8 -*-
import math

a=int(input('Informe o 1° número: '))
b=int(input('Informe o 2° número: '))
c=int(input('Informe o 3° número: '))
d=int(input('Informe o 4° número: '))

if a>b and c<=b and d<=c:
    print('S')
elif b>a and b>c and d<=c:
    print('S')
elif c>b and c>d and a<=b:
    print('S')
elif d>c and b<=c and a<=b:
    print('S')
else:
    print('N')
