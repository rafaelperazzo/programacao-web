# -*- coding: utf-8 -*-
import math
a=int(input('digite a:'))
b=int(input('digite b:'))
c=int(input('digite c:'))
a>=b>=c>0
if a<b+c:
    print('S')
elif a*2==(b*2)+(c*2):
    print('Re')
else:
    if a*2>(b*2)+(c*2):
        print('Ob')
    elif a*2<(b*2)+(c*2):
        print('Ac')
    else:
        if a==b==c:
            print('Eq')
        elif b==c!=a:
            print('Is')
        else:
            print('Es')
    else:
        print('N')
