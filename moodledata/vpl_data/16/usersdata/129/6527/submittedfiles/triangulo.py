# -*- coding: utf-8 -*-
from __future__ import division
import math
a= input('Digite o valor: ')
b= input('Digite o valor: ')
c= input('Digite o valor: ')
if a>=b>=c and a<b+c :
    print ('S')
    if a**2==(b**2)+(c**2):
        print ('Re')
    elif a**2>(b**2)+(c**2):
        print ('Ob')
    elif a**2<(b**2)+(c**2):
        print ('Ac')
    if a==b==c:
        print ('Eq')
    elif b==c!=a:
        print ('Is')
    elif a!=b!=c:
        print ('Es')
else:
    print ('N')
        