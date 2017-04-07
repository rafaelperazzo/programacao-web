# -*- coding: utf-8 -*-
a=int(input('Digite a:'))
b=int(input('Digite b:'))
c=int(input('Digite c:'))
d=int(input('Digite d:'))
if a>b and a>c and a>d:
    print('%d' %a)
    if b<c and b<d:
        print('%d'%b)
    if c<b and c<d:
        print('%d'%c)
    if d<b and d<c:
        print('%d'%d)
        