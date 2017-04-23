# -*- coding: utf-8 -*-
import math
a=int(input('Digite o comprimento a:'))
b=int(input('Digite o comprimento b:'))
c=int(input('Digite o comprimento c:'))

if a<(b+c) and (a>=b>=c):
    print('S')
    if (a**2)==((b**2)+(c**2)):
        print('Re')
    if (a**2)>((b**2)+(c**2)):
        print('Ob')
    if (a**2)<((b**2)+(c**2)):
        print('Ac')
        
    if a==b and b==c:
        print('Eq')
    if b==c and c!=a:
        print('Is')
    if a!=b and b!=c:
        print('Es')
        
else:
    print('N')