# -*- coding: utf-8 -*-
import math
a=int(input('Digite o valor do lado a: '))
b=int(input('Digite o valor do lado b: '))
c=int(input('Digite o valor do lado c: '))
if a>=b>=c>0:
    print('S')
    elif  a>=b>=c>0 and a**2==(b**2)+(c**2):
        print('Re')
    elif a>=b>=c>0 and (a**2)>(b**2)+(c**2):
        print('Ob')
    elif a>=b>=c>0 and (a**2)<(b**2)+(c**2):
        print('Ac')
    elif a>=b>=c>0 and a==b==c:
        print('Eq')
    elif a>=b>=c>0 and  b==c!=a:
        print('Is')
    elif a>=b>=c>0 and  a!=b!=c:
        print('Es')
    else:
        print('N')
    