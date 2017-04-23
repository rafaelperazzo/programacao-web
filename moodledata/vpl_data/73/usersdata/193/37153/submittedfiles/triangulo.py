 # -*- coding: utf-8 -*-
import math
a=int(input('digite o comprimento de a:'))
b=int(input('digite o comprimento de b:'))
c=int(input('digite o comprimento de c:'))
if a<b+c:
    print('S')
    if a**2==b**2+c**2:
        print('Re')
    if a**2>b**2+c**2:
        print('Ob')
    if a**2<b**2+c**2:
        print('Ac')
    if a==b==c:
        print('Eq')
    if b==c!=a:
        print('Is')
    if a!=b!=c:
        print('Es')
else:
    print('N')  