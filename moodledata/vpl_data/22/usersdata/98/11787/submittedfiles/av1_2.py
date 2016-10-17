# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('Digite o primeiro valor: '))
b=int(input('Digite o segundo valor: '))
c=int(input('Digite o terceiro valor: '))
d=int(input('Digite o quarto valor: '))


if a==c and b==d:
    print('F')
elif a!=b and a!=c and a!=d and b!=c and b!=d and c!=d:
    print('F')
elif a==b or b==c or c==d:
    print('F')
else:
    print('V')

