# -*- coding: utf-8 -*-
import math

a=int(input('Informe o 1° número: '))
b=int(input('Informe o 2° número: '))
c=int(input('Informe o 3° número: '))
d=int(input('Informe o 4° número: '))

if a>b and b>=c and c>=d:
    print('S')
elif b>a and b>c and c>=d:
    print('S')
elif c>b and c>d and b>=a:
    print('S')
elif d>c and c>=b and b>=a:
    print('S')
else:
    print('N')