# -*- coding: utf-8 -*-
import math
a=int(input('digite o comprimento do lado a:'))
b=int(input('digite o comprimento do lado b:'))
c=int(input('digite o comprimento do lado c:'))
if a<b+c:
    if (a*a)==(b*b)+(c*c):
        print('Re')
    elif (a*a)>(b*b)+(c*c):
        print('Ob')
    elif (a*a)<(b*b)+(c*c):
        print('Ac')
    elif a==b==c:
        print('Eq')
    elif b==c!=a:
        print('Is')
    elif a!=b!=c:
        print('Es')
else:
    print('N')