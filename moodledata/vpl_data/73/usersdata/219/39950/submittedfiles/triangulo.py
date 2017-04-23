# -*- coding: utf-8 -*-
import math
a=int(input('Digite o valor a:'))
b=int(input('Digite o valor b:'))
c=int(input('Digite o valor c:'))
if a<b+c:
    print('S')
    if a**2==b**2+c**2:
        print('Re')
    elif a**2>b**2+c**2:
        print('Ob')
    elif a**2<b**2+c**2:
        print('Ac')
            if a==b==c:
                print('Eq')
            elif a==b!=c:
                print('Is')
            elif a!=b!=c:
                print('Es')
else:
    print('N')
    