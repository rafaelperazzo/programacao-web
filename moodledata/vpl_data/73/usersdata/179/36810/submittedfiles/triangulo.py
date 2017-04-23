# -*- coding: utf-8 -*-
a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
c=int(input('digite o valor de c:'))
if a>b+c:
    print('N')
else:    
    if a**2==b**2+c**2 and a==b==c:
        print('s')
        print('Re')
        print('Eq')
    elif a**2==b**2+c**2 and  b==c!=a:
        print('s')
        print('Re')
        print('Is')
    elif a**2==b**2+c**2 and a!=b!=c:
        print('s')
        print('Re')
        print('Es')
    elif a**2>b**2+c**2 and a==b==c:
        print('s')
        print('Ob')
        print('Eq')
    elif a**2>b**2+c**2 and b==c!=a:
        print('s')
        print('Ob')
        print('Is')
    elif a**2>b**2+c**2 and a!=b!=c:
        print('s')
        print('Ob')
        print('Es')
    elif a**2<b**2+c**2 and a==b==c:
        print('s')
        print('Ac')
        print('Eq')
    elif a**2<b**2+c**2 and b==c!=a:
        print('s')
        print('Ac')
        print('Is')
    elif a**2<b**2+c**2 and a!=b!=c:
        print('s')
        print('Ac')
        print('Es')
    
    