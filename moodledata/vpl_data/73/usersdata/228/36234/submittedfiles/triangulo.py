# -*- coding: utf-8 -*-
import math
a=int(input('digite um valor:'))
b=int(input('digite um valor:'))
c=int(input('digite um valor:'))
if a>=b>=c>=0:
    print('S')
    if (a*a)==(b*b)+(c*c):
        print('Re')
    if (a*a)>(b*b)+(c*c):
        print('Ob')
    if (a*a)<(b*b)+(c*c):
        print('Ac')
    if a==b==c:
        print('Eq')
    if b==c!=a:
        print('Is')
    if a!=b!=c:
        print('Es')
else:
    print('N')

