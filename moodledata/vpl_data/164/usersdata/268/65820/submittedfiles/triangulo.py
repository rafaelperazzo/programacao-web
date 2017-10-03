# -*- coding: utf-8 -*-
import math

a= int(input('Digite o lado a '))
b= int(input('Digite o lado b '))
c= int(input('Digite o lado c '))

if (a> b + c) or (a == b + c):
    print('N')
else:
    print('S')
    if (a**2==b**2 + c**2):
        print('Re')
    if (a**2>b**2 + c**2):
        print('Ob')
    if (a**2<b**2 +c**2):
        print('Ac')
    if(a==b==c):
        print('Eq')
    if(b==c!=a):
        print('Is')
    if(a!=b!=c):
        print('Es')
    
    
    
    






    
