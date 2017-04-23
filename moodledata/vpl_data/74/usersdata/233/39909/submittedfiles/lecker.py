# -*- coding: utf-8 -*-
import math
a=int(input('Digite um número qualquer: '))
b=int(input('Digite um número qualquer: '))
c=int(input('Digite um número qualquer: '))
d=int(input('Digite um número qualquer: '))
if a==b==c==d:
    print('N')
if a>b and d<=c:
        print('S')
elif b>a and b>c and d<=c:
        print('S')
elif a<=c and b<c and d<c:
        print('S')
elif a<=c and b<=c and d>c:
    print('S')
    else: print('N')

    