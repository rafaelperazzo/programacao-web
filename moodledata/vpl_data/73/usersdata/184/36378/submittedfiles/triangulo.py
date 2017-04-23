# -*- coding: utf-8 -*-
import math
a=float(input('digite o valor de a:'))
b=float(input('digite o valor de b:'))
c=float(input('digite o valor de c:'))
if a<(b+c) and (a*a)==((b*b)+(c*c)) and a==b==c:
    print('S')
    print('Re')
    print('Eq')
elif a<(b+c) and (a*a)==((b*b)+(c*c)) and b==c!=a:
    print('S')
    print('Re')
    print('Is')
elif a<(b+c) and (a*a)==((b*b)+(c*c)) amd a!=b!=c:
    print('S')
    print('Re')
    print('Es')
else:
    if a<(b+c) and (a*a)>((b*b)+(c*c)) and a==b==c:
        print('S')
        print('Ob')
        print('Eq')
    elif a<(b+c) and (a*a)>((b*b)+(c*c)) and b==c!=a:
        print('S')
        print('Ob')
        print('Is')
    elif a<(b+c) and (a*a)>((b*b)+(c*c)) and a!=b!=c:
        print('S')
        print('Ob')
        print('Es')
    else:
        if a<(b+c) and (a*a)<((b*b)+(c*c)) and a==b==c:
            print('S')
            print('Ac')
            print('Eq')
        elif a<(b+c) and (a*a)<((b*b)+(c*c)) and b==c!=a:
            print('S')
            print('Ac')
            print('Is')
        elif a<(b+c) and (a*a)<((b*b)+(c*c)) and a!=b!=c:
            print('S')
            print('Ac')
            print('Es')
        else:
            print('N')