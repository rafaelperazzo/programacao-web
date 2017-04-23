# -*- coding: utf-8 -*-
import math
a=int(input('Digite a:'))
b=int(input('Digite b:'))
c=int(input('Digite c:'))
if (a>=b>=c>0) and (a<b+c):
    print('S')
    if (a*a==b*b+c*c):
        print('Re')
    if (a*a>b*b+c*c):
        print('Ob')
    if (a*a<b*b+c*c):
        print('Ac')
    if (a==b==c):
        print('Eq')
    if (b==c!=a):
        print('Is')
    if (a!=b!=c):
        print('Es')
else:
    print('N')
