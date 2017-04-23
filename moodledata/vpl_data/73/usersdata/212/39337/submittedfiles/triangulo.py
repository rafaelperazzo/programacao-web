# -*- coding: utf-8 -*-
import math
a=int(input('digite o valor do lado A(lado maior):'))
b=int(input('digite o valor do lado B:'))
c=int(input('digite o valor do lado C:'))
if a>=b and b>=c and c>0 and a<(b+c):
    print('S')
    if (a*a)==((b*b)+(c*c)):
        print('Re')
    if (a*a)>((b*b)+(c*c)):
        print('Ob')
    if (a*a)<((b*b)+(c*c)):
        print('Ac')
    if a==b and b==c:
        print('Eq')
    elif b=c and c!=a:
        print('Is')
    if a!=b and a!=c and c!=b:
        print('Es')
else:
    print('N')