# -*- coding: utf-8 -*-
a = float(input('Insira o peso da esfera A: '))
b = float(input('Insira o peso da esfera B: '))
c = float(input('Insira o peso da esfera C: '))
d = float(input('Insira o peso da esfera D: '))
if (a == b+c+d) and (b+c==d) and (b==c):
    print('S')
else:
    print('N')


