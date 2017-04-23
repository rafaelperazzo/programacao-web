# -*- coding: utf-8 -*-
a=int(input('digite a'))
b=int(input('digite b'))
c=int(input('digite c'))
if a>b+c:
    print('N')
else:
    if a**2==b**2+c**2 and a==b==c:
        print('S')
        print('Re')
        print ('Eq')
    elif a**2==b**2+c**2 and b==c!=a:
        print('S')
        print('Re')
        print ('Is')
    elif a**2==b**2+c**2 and a!=b!=c:
        print('S')
        print('Re')
        print ('Es')
    elif a**2>b**2+c**2 and a==b==c:
        print('S')
        print('Ob')
        print ('Eq')
    elif a**2>b**2+c**2 and b==c!=a:
        print('S')
        print('Ob')
        print ('Is')
    elif a**2>b**2+c**2 and a!=b!=c:
        print('S')
        print('Ob')
        print ('Es')
    elif a**2<b**2+c**2 and a==b==c:
        print('S')
        print('Ac')
        print ('Eq')
    elif a**2<b**2+c**2 and b==c!=a:
        print('S')
        print('Ac')
        print ('Is')
    elif a**2<b**2+c**2 and a!=b!=c:
        print('S')
        print('Ac')
        print ('Es')