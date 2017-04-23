# -*- coding: utf-8 -*-
import math
a=int(input('Digite o comprimento do lado a do triângulo: '))
b=int(input('Digite o comprimento do lado b do triângulo: '))
c=int(input('Digite o comprimento do lado c do triângulo: '))
if (a>=b) and (b>=c) and (c>0):
    print('Números positivos')
    if a<(b+c):
        print('S')
    else:
        print('N')
if (a**2)==(b**2)+(c**2):
    print('Re')
elif (a**2)>(b**2)+(c**2):
    print('Ob')
elif (a**2)<(b**2)+(c**2):
    print('Ac')
if (a==b) and (b==c):
    print(Eq)
elif (b==c) and (c!=a):
    print('Is')
elif (a!=b) and (b!=c):
    print('Es')

    
        
