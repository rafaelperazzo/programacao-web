# -*- coding: utf-8 -*-
import math
a=int(input('digite a: '))
b=int(input('digite b: '))
c=int(input('digite c: '))

if a>b+c or a==b+c:
    print('N')
if a<b+c:
    print('S')
    if a*a==b*b+c*c:
        print('Re')
    if a*a>b*b+c*c:
        print('Ob')
    if a*a<b*b+c*c:
        print('Ac')
        
    if (a==b) and (b==c):
        print('Eq')
    if (a==b) or (a==c) or (b==c):
        print('Is')
    if (a!=b) and (a!=c) and (b!=c):
        print('Es')