# -*- coding: utf-8 -*-
import math
a=int(input('digite o comprimento de a'))
b=int(input('digite o comprimento de b'))
c=int(input('digite o comprimento de c'))
if a<b+c:
    print('S')
    if a**2==b**2+c**2:
        print('Retângulo')
    if a**2>b**2+c**2:
        print('Obtusângulo')
    if a**2<b**2+c**2:
        print('acutângulo')
else:
    print('N')
    if a==b==c:
        print('equilátero')
    if b==c=!c:
        print('isósceles')
    if a=!b=!c:
        print('escaleno')