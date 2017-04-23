# -*- coding: utf-8 -*-
a=float(input('Informe o peso da esfera A: '))
b=float(input('Informe o peso da esfera B: '))
c=float(input('Informe o peso da esfera C: '))
d=float(input('Informe o peso da esfera D: '))

if a==b+c+d and d==b+c and b==c:
    print('S')
else:
    print('N')