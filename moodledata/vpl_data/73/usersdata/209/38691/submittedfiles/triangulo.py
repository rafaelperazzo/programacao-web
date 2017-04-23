# -*- coding: utf-8 -*-
import math
a=int(input('Digite o lado A:'))
b=int(input('Digite o lado B:'))
c=int(input('Digite o lado C:'))
if a<b+c:
    print('S')
    if a**2>b**2+c**2:
        print('Ob')
    elif a**2<b**2+c**2:
        print('Ac')
    elif a=b:
        if b=c:
        print('Eq')
        else:
            print('Is')
    elif a>b or a<b:
        print('Es')