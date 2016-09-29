# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
a=int(input('Digite o valor de a:'))
b=int(input('Digite o valor de b:'))
c=int(input('Digite o valor de c:'))
#PROCESSAMENTO
if a<=(b+c):
    if a>=b and a>=c and b>=c and b>=0 and c>=0:
    print('S')
    if a**2==(b**2+c**2):
        print('Re')
        if a==b and b==c:
            print('Eq')
        elif b==c and c!=a:
            print('Iso')
        else:
            print('ES')
    elif a**2>(b**2+c**2):
        print('O')
        if a==b and b==c:
            print('Eq')
        elif b==c and c!=a:
            print('Iso')
        else:
            print('ES')
    else:
        print('Ac')
        if a==b and b==c:
            print('Eq')
        elif b==c and c!=a:
            print('Iso')
        else:
            print('ES')
else:
    print('N')