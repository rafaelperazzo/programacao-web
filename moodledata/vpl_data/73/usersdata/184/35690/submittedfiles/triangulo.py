# -*- coding: utf-8 -*-
import math
a=float(input('digite o valor de a:'))
b=float(input('digite o valor de b:'))
c=float(input('digite o valor de c:'))
if a>(b+c):
    print('N')
else:
    if a<(b+c) and (a*a)==((b*b)+(c*c)) and a==b==c:
        print('S')
        print('Re')
        print('Eq')
    elif a<(b+c) and (a*a)>((b*b)+(c*c)) and b==c!=a:
        print('S')
        print('Ob')
        print('Is')
    else:
        if a<(b+c) and (a*a)<((b*b)+(c*c)) and a!=b!=c:
            print('S')
            print('Ac')
            print('Es')
        