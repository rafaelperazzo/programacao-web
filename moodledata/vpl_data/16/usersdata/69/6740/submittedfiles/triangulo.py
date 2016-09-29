# -*- coding: utf-8 -*-
from __future__ import division
import math
a=int(input('Digite o valor de a:'))
b=int(input('Digite o valor de b:'))
c=int(input('Digite o valor de c:'))
if a<(b+c):
    print('S')
    if (a*a)==((b*b)+(c*c)):
        print('Re')
    elif (a*a)>((b*b)+(c*c)):
        print('Ob')
    else:
        print('Ac')
    if a==b==c:
        print('Eq')
    elif b==c!=a:
        print('Is')
    else:
        print('Es')
else:
    print('N')