# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('Digite o primeiro valor: '))
b=int(input('Digite o segundo valor: '))
c=int(input('Digite o terceiro valor: '))

if a>=b+c:
    print ('N')

else:
    print ('S')
    if (a**2)==(b**2)+(c**2):
        print ('Re')
    elif (a**2)>(b**2)+(c**2):
        print ('Ob')
    else:
        print ('Ac')
    
    if a==b and b==c:
        print ('Eq')
    elif b==c and c!=a:
        print ('Is')
    elif a!=b and a!=c:
        print ('Es')