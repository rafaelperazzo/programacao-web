# -*- coding: utf-8 -*-
a=float(input('Digite a:'))
b=float(input('Digite b:'))
c=float(input('Digite c:'))
if b>=c>=a:
    print('%.2f'%a)
    print('%.2f'%c)
    print('%.2f'%b)
if c>=b>=a:
    print('%.2f'%a)
    print('%.2f'%b)
    print('%.2f'%c)
if b>=a>=c:
    print('%.2f'%c)
    print('%.2f'%a)
    print('%.2f'%b)
if c>=a>=b:
    print('%.2f'%b)
    print('%.2f'%a)
    print('%.2f'%c)
if a>=b>=c:
    print('%.2f'%c)
    print('%.2f'%b)
    print('%.2f'%a)