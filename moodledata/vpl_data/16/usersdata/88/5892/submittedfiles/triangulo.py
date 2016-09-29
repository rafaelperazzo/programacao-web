# -*- coding: utf-8 -*-
from __future__ import division
import math

a= input('digite um valor: ')
b= input('digite um valor: ')
c= input('digite um valor: ')

if a>=b>=c>0:
    print('S')
    if (a*2)==(b*2)+(c*2):
        print('Re')
    if (a*2)>(b*2)+(c*2):
        print('Ob')
    if (a*2)<(b*2)+(c*2):
        print('Ac')
    if a==b==c:
        print('Eq')
    if b==c!=a:
        print('Is')
    if a!=b!=c:
        print('Es')
else:
    print('N')

    
