# -*- coding: utf-8 -*-
import math
a=int(input('digite a:'))
b=int(input('digite b:'))
c=int(input('digite c:'))
if a*a==b*b+c*c:
    print('retângulo')
elif a*a>b*b+c*c:
    print('obtusângulo')
elif a*a<b*b+c*c:
    print('acutângulo')
if a==b==c:
    print('equilátero')
elif b==c!=a:
    print('isósceles')
elif a!=b!=c:
    print('escaleno')