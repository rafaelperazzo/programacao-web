# -*- coding: utf-8 -*-
import math
a=int(input('Digite a: '))
b=int(input('Digite b: '))
c=int(input('Digite c: '))

if a>b+c or a==b+c:
    print ('N')
if a<b+c:
    print('S')
    if a*a==b*b=c*c:
    print('Re')
    if a*a>b*b+c*c:
        print('Ob')
    if a*a<b*b+c*c:
        print('Ac')

    if (a==b) and (b==c):
        print('Eq')
    if (a==b) and (a!=c) or (a==c) and (a!=c) or (b==c) and (a!=b):
        print('Is')
    if (a!=b) and (a!=c) and (b!=c):
        print('Es')