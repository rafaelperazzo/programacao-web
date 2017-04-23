# -*- coding: utf-8 -*-
import math
a=int(input('Digite a: '))
b=int(input('Digite b: '))
c=int(input('Digite c: '))
if (a=b+c):
    quadradoA=a**2
    quadradoB=b**2
    quadradoC=c**2
    d=quadradoB+quadradoC
    print('S')
    if (quadradoA==d):
        print('Re')
    elif (quadradoA>d):
        print('Ob')
    else:
        print('Ac')
    if (a==b==c):
        print('Eq')
    elif (b==c!=a):
        print('Is')
    else:
        print('Es')
else:
    print('N')