# -*- coding: utf-8 -*-
import math
a=int(input('digite um valor:'))
b=int(input('digite um valor:'))
c=int(input('digite um valor:'))
a2=(a**2)
b2=(b**2)
c2=(c**2)
if  a<b+c or b<a+c or c<b+a:
    if a2==b2+c2 or b2==c2+a2 or c2==b2+a2:
        print('Re')
    if a2>b2+c2 or b2>c2+a2 or c2>b2+a2:
        print('Ob')
    if a2<b2+c2 or b2<a2+c2 or c2<a2+b2:
        print('Ac')
else:
    print('N')
