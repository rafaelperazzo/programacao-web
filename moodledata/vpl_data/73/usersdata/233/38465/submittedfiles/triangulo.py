# -*- coding: utf-8 -*-
import math
a=int(input('Digite um número qualquer: '))
b=int(input('Digite um número qualquer: '))
c=int(input('Digite um número qualquer: '))
if a<(b+c) and b<(c+a) and c<(a+b) and a>=b>=c:
    print('S')
    if (a**2)==(b**2)+(c**2) and a==b==c:
        print('Re')
        print('Eq')
    elif (a**2)>(b**2)+(c**2) and a==b==c:
        print('Ob')
        print('Eq')
    elif (a**2)<(b**2)+(c**2) and a==b==c:
        print('Ac')
        print('Eq')
    if (a**2)==(b**2)+(c**2) and a!=b==c:
        print('Re')
        print('Eq')
    elif (a**2)>(b**2)+(c**2) and a!=b==c:
        print('Ob')
        print('Is')
    elif (a**2)<(b**2)+(c**2) and a!=b==c:
        print('Ac')
        print('Is')
    if (a**2)==(b**2)+(c**2) and a!=b!=c:
        print('Re')
        print('Es')
    elif (a**2)>(b**2)+(c**2) and a!=b!=c:
        print('Ob')
        print('Es')
    elif (a**2)<(b**2)+(c**2) and a!=b!=c:
        print('Ac')
        print('Es') 
else:
    print('N')
       
        
     