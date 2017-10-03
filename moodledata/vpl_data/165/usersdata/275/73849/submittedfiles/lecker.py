# -*- coding: utf-8 -*-
import math
a= int(input( 'Digite o valor  : '))
b= int(input( 'Digite o valor  : '))
c= int(input( 'Digite o valor  : '))
d= int(input( 'Digite o valor  : '))

if a>b:
    if a>c:
        if a>d:
            print('S')
elif b>a:
    if b>c:
        if b>d:
            print('S')
elif c >a:
    if c>b:
        if c>d:
            print('S')
elif d> a:
    if d>b:
        if d>c:
            print('S')
else:
    print('N')