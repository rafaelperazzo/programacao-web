# -*- coding: utf-8 -*-
from __future__ import division
import math

#entrada
a = int(input('digite o valor de a:'))
b = int(input('digite o valor de b:'))
c = int(input('digite o valor de c:'))

if a>=b>=c>0 and a<b+c:
    print ('S')
    if a**2==b**2==c**2:
        if a==b==c:
            print('Re')
            print('Eq')
        elif b==c!=a:
            print('Re')
            print('Is')
        elif a!=b!=c:
            print('Re')
            print('Es')      
    elif a**2>b**2+c**2:
        if a==b==c:
            print('Ob')
            print('Eq')
        elif b==c!=a:
            print('Ob')
            print('Is')
        elif a!=b!=c:
            print('Ob')
            print('Es') 
    elif a**2<b**2+c**2:
        if a==b==c:
            print('Ac')
            print('Eq')
        elif b==c!=a:
            print('Ac')
            print('Is')
        elif a!=b!=c:
            print('Ac')
            print('Es') 
else:
    print('N')
