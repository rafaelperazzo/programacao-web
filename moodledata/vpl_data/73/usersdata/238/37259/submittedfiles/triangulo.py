# -*- coding: utf-8 -*-
import math
a=int(input('digite o complemento de a:'))
b=int(input('digite o complemento de b:'))
c=int(input('digite o complemento de c:'))
if a<b+c:
    print('s')
    if a**2==b**2+c**2:
        print('re')
    if a**2>b**2+c**2:
        print('ob')
    if a**2<b**2+c**2:
        print('ac')
    if a==b==c:
        print('eq')
    if b==c!=a:
        print('is')
    if a!=b!=c:
        print('es')
else:
    print('n')
    