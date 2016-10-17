# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('Digite o primeiro valor: '))
b=int(input('Digite o segundo valor: '))
c=int(input('Digite o terceiro valor: '))
d=int(input('Digite o quarto valor: '))

if a==c or b==d:
    print('V')
elif a==b and b==c and c==d:
    print('F')
else:
    print('F')

