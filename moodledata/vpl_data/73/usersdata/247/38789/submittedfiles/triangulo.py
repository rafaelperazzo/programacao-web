# -*- coding: utf-8 -*-
import math
a=int(input('digite a: '))
b=int(input('digite b: '))
c=int(input('digite c: '))
if a>=b>=c>0 and a<b+c:
    print('S')
    if a*a==b*b+c*c:
        print('Re')
        if a==b==c:
            print('Eq')
        elif a!=c==b:
            print('Is')
        elif a!=b!=c:
            print('Es')
    elif a*a>b*b+c*c:
        print('Ob')
        if a==b==c:
            print('Eq')
        elif a!=c==b:
            print('Is')
        elif a!=b!=c:
            print('Es')
    elif a*a<b*b+c*c:
        print('Ac')
        if a==b==c:
            print('Eq')
        elif a!=c==b:
            print('Is')
        elif a!=b!=c:
            print('Es')
else:
    print('N')
        