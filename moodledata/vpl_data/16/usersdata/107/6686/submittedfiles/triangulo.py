# -*- coding: utf-8 -*-
from __future__ import division
import math
a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
c=int(input('digite o valor de c:'))
if a<b+c and b<a+c and c<a+b:
    print('S')
    if ((a**2)==(b**2)+(c**2)) or ((b**2)==(a**2)+(c**2)) or ((c**2)==(b**2)+(a**2)):
        print('Re')
        if a==b and b==c:
             print('Eq')
        if b==c and c!=a:
            print('Is')
        else:
            print('Es')
    elif ((a**2)>(b**2)+(c**2)) or ((b**2)>(a**2)+(c**2)) or ((c**2)>(b**2)+(a**2)):
    print('Ob')
       if a==b and b==c:
             print('Eq')
        if b==c and c!=a:
            print('Is')
        else:
            print('Es')
    else:
    print('Ac')
else:
    ('N')

