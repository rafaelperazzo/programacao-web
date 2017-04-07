# -*- coding: utf-8 -*-
a=float(input('digite um numero:'))
b=float(input('digite outro numero:'))
c=float(input('digite outro numero:'))
if a<b and a<c and b<c:
    print('%.0f'%a)
    print('%.0f'%b)
    print('%.0f'%c)
if a>b and a>c and b>c:
    print('%.0f'%c)
    print('%.0f'%b)
    print('%.0f'%a)
if b<a and b<c and c<a:
    print('%.0f'%b)
    print('%.0f'%c)
    print('%.0f'%a)
if b<a and b<c and a<c:
    print('%.0f'%b)
    print('%.0f'%a)
    print('%.0f'%c)
if c<a and c<b and b>a:
    print('%.0f'%c)
    print('%.0f'%a)
    print('%.0f'%b)
if a<c and a<b and c<b:
    print('%.0f'%a)
    print('%.0f'%c)
    print('%.0f'%b)