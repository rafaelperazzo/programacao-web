# -*- coding: utf-8 -*-
from __future__ import division
import math

a = int(input('Digite um valor inteiro "a":'))
b = int(input('Digite um valor inteiro "b":'))
c = int(input('Digite um valor inteiro "c":'))

if a>=b and b>=c and c>0:
    if (b+c)>a:
        print ('S')
        if a**2 ==(b**2+c**2):
            print ('Re')
        elif a**2 >(b**2+c**2):
            print ('Ob')
        elif a**2 <(b**2+c**2):
            print ('Ac')
        if a==b and b==c:
            print ('Eq')
        elif b==c and c!=a:
            print ('Is')
        elif a!=b and b!=c:
            print ('Es')
else:
    print ('N')