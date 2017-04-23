# -*- coding: utf-8 -*-
import math
a=int(input('Digite um número qualquer: '))
b=int(input('Digite um número qualquer: '))
c=int(input('Digite um número qualquer: '))
d=int(input('Digite um número qualquer: '))
if a>b:
    if b>c and c>d:
        print('S')
    if b==c==d:
        print('S')
elif d>c:
    if c>b and b>a:
        print('S')
    elif c==b==a:
        print('S')
elif b>a:
    if b>c and c>d:
        print('S')
    elif b==c==d:
        print('S')
elif c>b:
    if c>d and b>a:
        print('S')
    elif b==d==a:
        print('S')
else: 
    print('N')
    