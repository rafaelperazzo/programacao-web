# -*- coding: utf-8 -*-
import math

a=int(input('Digite o valor a:'))
b=int(input('Digite o valor de b:'))
c=int(input('Digiteo valor de c:'))

if a<(b+c):
    print('S')
    if a**2==((b**2)+(c**2)):
        print('Re')
    elif (a**2)>((b**2)+(c**2)):
        print('Ob')
    elif (a**2)<((b**2)+(c**2)):
        print('Ac')
    if a==b and b==c:
        print('Eq')
    elif b==c and c!=a:
        print('Is')
    elif a!=b and b!=c:
        print('Es')
else:
    print('N')