# -*- coding: utf-8 -*-
import math

a=float(input('Digite o número a: '))
b=float(input('Digite o número b: '))
c=float(input('Digite o número c: '))
d=float(input('Digite o número d: '))

if a<b and b<c and c<d:
    print('S')
elif a<b and b>c and c>d:
    print('S')
elif a<b and b<c and c>d:
    print('S')
elif a>b and b>c and c>d:
    print('S')
elif a<b and b==c and b==d:
    print('S')
elif a<b and a==c and a==d:
    print('S')
elif a<b and a==c and c==d:
    print('S')
elif a<b and b==c and b==d:
    print('S')
elif c>a and a==b and b==d:
    print('S')
elif c>a and c==b and c==d:
    print('S')
elif d>a and a==b and b==c:
    print('S')
else:
    print('N')