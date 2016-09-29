# -*- coding: utf-8 -*-
from __future__ import division
import math
a= int(input(' digite o valor do lado do triangulo sendo maior igual a zero:'))
b= int(input(' digite o valor do lado do triangulo sendo maior igual a zero:'))
c= int(input(' digite o valor do lado do triangulo sendo maior igaul a zero:'))
if a<(b+c):
    print('S')
    if (a**2)==(b**2)+(c**2):
                        print('Re')
    if (a**2)>(b**2)+(c**2):
                        print('Ob')
    if (a**2)<(b**2)+(c**2):   
                        print('Ac')
    if a==b==c:
        print('Eq')
    if b==c!=a:
        print('Is')
        if a!=b!=c:
            print('Es')
else:
    print('N')    