# -*- coding: utf-8 -*-
a=float(input('digite um numero:'))
b=float(input('digite outro numero:'))
c=float(input('digite outro numero:'))
if a<b and a<c and b<c:
    print('%.1f'%a)
    print('%.1f'%b)
    print('%.1f'%c)
if a>b and a>c and b>c:
    print('%.1f'%c)
    print('%.1f'%b)
    print('%.1f'%a)
if b<a and b<c and c<a:
    print('%.1f'%b)
    print('%.1f'%c)
    print('%.1f'%a)
if b<a and b<c and a<c:
    print('%.1f'%b)
    print('%.1f'%a)
    print('%.1f'%c)
if c<a and c<b and b>a:
    print('%.1f'%c)
    print('%.1f'%a)
    print('%.1f'%b)
if a<c and a<b and c<b:
    print('%.1f'%a)
    print('%.1f'%c)
    print('%.1f'%b)