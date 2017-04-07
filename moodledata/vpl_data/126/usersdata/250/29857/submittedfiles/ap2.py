# -*- coding: utf-8 -*-
a=float(input('digite a:'))
b=float(input('digite b:'))
c=float(input('digite c:'))
d=float(input('digite d:'))
if a>b and a>c and a>d and b<c:
    print('%.0f'%a)
    print('%.0f'%b)
if a>b and a>c and a>d and b>c:
    print('%.0f'%a)
    print('%.0f'%c)