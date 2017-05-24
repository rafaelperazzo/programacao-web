# -*- coding: utf-8 -*-
import math
a=int(input('digite o primeiro numero:'))
b=int(input('digite o segundo numero:'))
c=int(input('digite o terceiro numero:'))
d=int(input('digite o quarto numero:'))

if a==c and b!=d and a!=b:
    print('V')
elif b==d and a!=c and a!=b and c!=d:
    print('V')
else:
    print('F')
