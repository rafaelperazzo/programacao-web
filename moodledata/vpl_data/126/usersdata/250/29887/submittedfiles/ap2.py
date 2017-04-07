# -*- coding: utf-8 -*-
a=float(input('digite a:'))
b=float(input('digite b:'))
c=float(input('digite c:'))
d=float(input('digite d:'))
if a>b and a>c and a>d and b<c and b<d:
    print('%.0f'%a)
    print('%.0f'%b)
if a>b and a>c and a>d and b>c and c<d:
    print('%.0f'%a)
    print('%.0f'%c)
if a>b and a>c and a>d and b>d and c>d:
    print('%.0f'%a)
    print('%.0f'%d)
if b>a and b>c and b>d and a<c and a<d:
    print('%.0f'%b)
    print('%.0f'%a)
if b>a and b>c and b>d and a>c and c<d:
    print('%.0f'%b)
    print('%.0f'%c)
if b>a and b>c and b>d and d<c and a>d:
    print('%.0f'%b)
    print('%.0f'%d)
if c>a and c>b and c>d and a<b and a<d:
    print('%.0f'%c)
    print('%.0f'%a)
if c>a and c>b and c>d and a>b and B<d:
    print('%.0f'%c)
    print('%.0f'%b)
if c>a and c>b and c>d and d<b and a>d:
    print('%.0f'%c)
    print('%.0f'%d)
if d>a and d>b and c<d and a<b and a<c:
    print('%.0f'%d)
    print('%.0f'%a)
if d>a and d>b and c<d and a>b and b<c:
    print('%.0f'%d)
    print('%.0f'%b)
if d>a and d>b and c<d and c<b and a>c:
    print('%.0f'%d)
    print('%.0f'%a)
    