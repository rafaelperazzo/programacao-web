# -*- coding: utf-8 -*-
import math
a=int(input('digite a:'))
b=int(input('digite b:'))
c=int(input('digite c:'))
if a<b+c:
    print('S')
    if a*a==b*b+c*c:
        print('Re')
    elif a*a>b*b+c*c:
        print('Ob')
    elif a*a<b*b+c*c:
        print('Ac')
    if a==b==c:
        print('Eq')
    elif b==c!=a:
        print('Is')
    elif a!=b!=c:
        print('Es')
else:
    print('N')
