# -*- coding: utf-8 -*-
import math
a=int(input('digite um valor:'))
b=int(input('digite um valor:'))
c=int(input('digite um valor:'))
a2=(a**2)
b2=(b**2)
c2=(c**2)
if  a<b+c:
    print('S')
    if a2==b2+c2:
        print('Re')
    elif a2>b2+c2:
        print('Ob')
    else:
        print('Ac')
elif    a>b+c:
        print('N')
if  a==b==c:
    print('Eq')
if  b==c!=a:
    print('Is')
if  a!=b!=c and a<b+c:
    print('Es')