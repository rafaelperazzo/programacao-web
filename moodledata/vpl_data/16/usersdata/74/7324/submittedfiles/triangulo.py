# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Primeiro valor')
b = input('Segundo valor')
c = input('Terceiro valor')

a1 = b+c
a2 = b**2+c**2
h = a**2

if a1>a:
    print('S')
    if a == b and b == c:
        print('Eq')
        print('Ac')
    elif b == c and a != c:
        print('Is')
        if a2 == h:
            print('Re')
        elif h > a2:
            print('O')
        else:
            print('Ac')
    else:
        print('Es')
        if a2 == h:
            print('Re')
        elif h > a2:
            print('O')
        else:
            print('Ac')
else:
    print('N')