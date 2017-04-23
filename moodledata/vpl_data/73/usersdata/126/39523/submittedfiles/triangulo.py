# -*- coding: utf-8 -*-
import math

a= float(input(' digite o comprimento de a:'))
b= float(input(' digite o comprimento de b:'))
c= float(input(' digite o comprimento de c:'))

if a>=b+c:
    print('N')
else:
    print('S')
    if (a**2)==(b**2)+(c**2):
        print('Re')
    elif (a**2)>(b**2)+(c**2):
        print('Ob')
    elif (a**2)<(b**2)+(c**2):
        print('Ac')
    if a==b==c:
        print('Eq')
    elif b==c and c!=a:
        print('Is')
    elif a!=b and b!=c and c!=a:
        print('Es')