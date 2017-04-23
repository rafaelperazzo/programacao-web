# -*- coding: utf-8 -*-
import math
a=int(input('Valor de A:'))
b=int(input('Valor de B:'))
c=int(input('Valor de C:'))
if a<b+c:
    QuadradoA=a**2
    QuadradoB=b**2
    QuadradoC=c**2
    d=QuadradoB+QuadradoC
    print('S')
    if QuadradoA==d:
       print('Re')
    elif QuadradoA>d:
       print('Ob')
    else:
       print('Ac')
    if a==b==c:
       print('Eq')
    elif b==c!=a:
       print('Is')
    else:
       print('Es')
else:
    print('N')
