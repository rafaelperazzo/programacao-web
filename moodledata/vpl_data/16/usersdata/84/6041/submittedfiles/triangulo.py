# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('valor de a:'))
b=int(input('valor de b:'))
c=int(input('valor de c:'))

if(a<b+c):
    print('S')
    if(a**2==(b**2)+(c**2)):
        print('Re')
    if((a**2)>(b**2)+(c**2)):
        print('Ob')
    if((a**2)<(b**2)+(c**2)):
        print('Ac')
    if(a==b==c):
        print('Eq')
    if(b==c!=a):
        print('Is')
    else:
        print('Es')
else:
    print('N')
        
