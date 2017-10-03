# -*- coding: utf-8 -*-
import math

a= float(input('Digite o valor do lado maior a: '))
b=float(input('Digite o valor do lado médio b: '))
c=float(input('Digite o valor do lado menor c: '))

if (a<b+c):
    print ('S')
    if ((a**2)==(b**2)+(c**2)):
        print ('Re')
    elif ((a**2)>(b**2)+(c**2)):
        print('Ob')
    elif ((a**2)<(b**2)+(c**2)):
        print('Ac')
    if (a==b==c):
        print ('Eq')
    elif (b==c!=a):
        print ('Is')
    elif (a!=b!=c):
        print ('Es')
else:
    print('N')

