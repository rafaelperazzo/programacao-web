# -*- coding: utf-8 -*-
import math
a=int(input('Digite a: '))
b=int(input('Digite b: '))
c=int(input('Digite c: '))
if (a>=b>=c>0):
    quadradoA=a**2
    quadradoB=b**2
    quadradoC=c**2
    d=quadradoB+quadradoC
    if (quadradoA==d):
        print('Re')
    elif (quadradoA>d):
        print('Ob')
    else:
        print('Ac')