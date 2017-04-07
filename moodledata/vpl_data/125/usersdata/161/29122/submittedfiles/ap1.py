# -*- coding: utf-8 -*-
a=float(input('Digite o valor de a:'))
b=float(input('Digite o valor de b:'))
c=float(input('Digite o valor de c:'))
if a>b and a>c and b>c:
    print('%.2f'%c)
    print('%.2f'%b)
    print('%.2f'%a)
if a>b and a>c and c>b: 
    print('%.2f' %b)
    print('%.2f'%c)
    print('%.2f'%a)
if b>a and b>c and a>c:
    print('%.2f'%c)
    print('%.2f'%a)
    print('%.2f'%b)
if b>a and b>c and c>a:
    print('%.2f' %a)
    print('%.2f'%c)
    print('%.2f'%b)
if c>a and c>b and a>b:
    print('%.2f'%b)
    print('%.2f'%a)
    print('%.2f'%c)
if c>a and c>b and b>a:
    print('%.2f'%a)
    print('%.2f'%b)
    print('%.2f'%c)