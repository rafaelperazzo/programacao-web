# -*- coding: utf-8 -*-
a=float(input('Digite a:'))
b=float(input('Digite b:'))
c=float(input('Digite c:'))
d=float(input('Digite d:'))
if a>b and a>c and a>d:
    print('%f' %a)
    if a<b and a<c and a<d:
        print('%f' %a)
if b>a and b>c and b>d:
    print('%f' %b)
    if b<a and b<c and b<d:
        print('%f' %b)
if c>a and c>b and c>d:
    print('%f' %c)
    if c<a and c<b and c<d:
        print('%f')
else:
    print('%f' %d')
        