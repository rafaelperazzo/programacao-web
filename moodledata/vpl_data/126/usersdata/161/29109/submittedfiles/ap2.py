# -*- coding: utf-8 -*-
a=float(input('Digite a:'))
b=float(input('Digite b:'))
c=float(input('Digite c:'))
d=float(input('Digite d:'))
if a>b and a>c and a>d:
    print('%.2f' %a)
    if a<b and a<c and a<d:
        print('%.2f' %a)
if b>a and b>c and b>d:
    print('%.2f' %b)
    if b<a and b<c and b<d:
        print('%.2f' %b)
if c>a and c>b and c>d:
    print('%.2f' %c)
    if c<a and c<b and c<d:
        print('%.2f')
if d>a and d>b and b>c:
    print('%.2f' %d)
    if d<a and d<b and d<c:
        print('%.2f' %d')
        