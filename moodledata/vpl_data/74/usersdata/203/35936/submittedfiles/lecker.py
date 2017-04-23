# -*- coding: utf-8 -*-
import math
a=int(input('digite o primeiro valor: '))
b=int(input('digite o segundo valor: '))
c=int(input('digite o terceiro valor: '))
d=int(input('digite o quarto valor: '))
if a>b and b<c and c<d:
    print('S')
elif d>c and c>b and b>a:
    print('S')
elif b>a and b>c and c<d:
    print('S')
elif c>d and c>b and b<a:
    print('S')
else:
    print('N')