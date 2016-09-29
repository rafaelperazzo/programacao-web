# -*- coding: utf-8 -*-
from __future__ import division
import math

a= int(input('Digite o valor de a: '))
b= int(input('Digite o valor de b: '))
c= int(input('Digite o valor de c: '))

if a<b+c:
    print ('S')
    if (a**2)==(b**2)+(c**2):
       print ('Re')
       if  b==c!=a:
           print('Is')
        elif a!=b!=c:
            print('Es')
    elif (a**2)>(b**2)+(c**2):
        print('Ob')
        if  b==c!=a:
           print('Is')
        elif a!=b!=c:
            print('Es')
    elif (a**2)<(b**2)+(c**2):
        print('Ac')
        if a==b==c:
            print('Eq')
        if  b==c!=a:
           print('Is')
        elif a!=b!=c:
            print('Es')
else:
    print('N')
    
    