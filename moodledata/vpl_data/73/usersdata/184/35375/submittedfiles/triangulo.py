# -*- coding: utf-8 -*-
import math
a=float(input('digite o valor de a:'))
b=float(input('digite o valor de b:'))
c=float(input('digite o valor de c:'))
if a>(b+c):
    print('N')
else:
    if a<(b+c):
        print('S')
    else:
        if (a*a)==((b*b)+(c*c)):
            print('Re')
        elif (a*a)>((b*b)+(c*c)):
            print('Ob')
        else:
            if (a*a)<((b*b)+(c*c)):
                print('Ac')
            else:
                if a==b==c:
                    print('Eq')
                elif b==c!=a:
                    print('Is')
                else:
                    if a!=b!=c:
                        print('Es')