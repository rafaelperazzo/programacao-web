# -*- coding: utf-8 -*-
import math
a=int(input('Digite o comprimento de a:'))
b=int(input('Digite o comprimento de b:'))
c=int(input('Digite o comprimento de c:'))
if a>b+c or (a<=0) or (b<=0) or (c<=0):
    print('N')
elif (a**2)==(b**2)+(c**2):
    print('S')
    print('Re')
    if a==b==c:
    print('Eq')
    elif b==c!=a:
    print('Is')
    elif a!=b!=c:
    print('Es')
elif (a**2)>(b**2)+(c**2):
    print('S')
    print('Ob')
    if a==b==c:
    print('Eq')
    elif b==c!=a:
    print('Is')
    elif a!=b!=c:
    print('Es')
elif (a**2)<(b**2)+(c**2):
    print('S')
    print('Ac')
    if a==b==c:
    print('Eq')
    elif b==c!=a:
    print('Is')
    elif a!=b!=c:
    print('Es')
