# -*- coding: utf-8 -*-
a=float(input('Digite a:'))
b=float(input('Digite b:'))
c=float(input('Digite c:'))
if a>b:
    print('%.2f'%a)
    print('%.2f'%b)
elif b>a:
    print('%.2f'%b)
    print('%.2f'%a)
if a>c:
    print('%.2f'%a)
    print('%.2f'%c)
elif c>a:
    print('%.2f'%c)
    print('%.2f'%a)
if b>c:
    print('%.2f'%b)
    print('%.2f'%c)
elif c>b:
    print('%.2f'%c)
    print('%.2f'%b)