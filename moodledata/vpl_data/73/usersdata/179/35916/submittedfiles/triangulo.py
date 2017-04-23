# -*- coding: utf-8 -*-
import math
a=float(input('digite o valor de a:'))
b=float(input('digite o valor de b:'))
c=float(input('digite o valor de c:'))
if a<b+c:
    print('S')
else:
    if a**2==b**2+c**2 and a==b==c:
        print('Re')
        print('Eq')
    elif a**2==b**2+c**2 and  b==c!=a:
        print('Re')
        print('Is')
    elif a**2==b**2+c**2 and a!=b!=c:
        print('Re')
        print('Es')
    elif a**2>b**2+c**2 and a==b==c:
        print('Ob')
        print('Eq')
    elif a**2>b**2+c**2 and b==c!=a:
        print('Ob')
        print('Is')
    elif a**2>b**2+c**2 and a!=b!=c:
        print('Ob')
        print('Es')
    elif a**2<b**2+c**2 and a==b==c:
        print('Ac')
        print('Eq')
    elif a**2<b**2+c**2 and b==c!=a:
        print('Ac')
        print('Is')
    elif a**2<b**2+c**2 and a!=b!=c:
        print('Ac')
        print('Es')
    else:    
        if a>b+c:
            print('N')
    