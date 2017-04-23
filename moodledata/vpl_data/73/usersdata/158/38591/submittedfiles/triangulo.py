# -*- coding: utf-8 -*-
import math
a=int(input('digite a:'))
b=int(input('digite b:'))
c=int(input('digite c:'))
if a<b+c and (a*a)==(b*b)+(c*c) and a==b==c:
    print('S')
    print('Re')
    print('Eq')
elif a<b+c and (a*a)==(b*b)+(c*c) and b==c!=a:
    print('S')
    print('Re')
    print('Is')
elif a<b+c and (a*a)==(b*b)+(c*c) and a!=b!=c:
    print('S')
    print('Re')
    print('Es')
else:
    if a<b+c and (a*a)>(b*b)+(c*c) and a==b==c:
        print('S')
        print('Ob')
        print('Eq')
    elif a<b+c and (a*a)>(b*b)+(c*c) and b==c!=a:
        print('S')
        print('Ob')
        print('Is')
    elif a<b+c and (a*a)>(b*b)+(c*c) and a!=b!=c:
        print('S')
        print('Ob')
        print('Es')
    else:
        if a<b+c and (a*a)<(b*b)+(c*c) and a==b==c:
            print('S')
            print('Ac')
            print('Eq')
        elif a<b+c and (a*a)<(b*b)+(c*c) and b==c!=a:
            print('S')
            print('Ac')
            print('Is')
        elif a<b+c and (a*a)<(b*b)+(c*c) and a!=b!=c:
            print('S')
            print('Ac')
            print('Es')
        else:
            print('N')