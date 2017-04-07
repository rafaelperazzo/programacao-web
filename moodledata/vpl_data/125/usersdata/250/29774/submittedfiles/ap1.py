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