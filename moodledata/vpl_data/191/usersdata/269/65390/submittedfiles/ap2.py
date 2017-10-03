# -*- coding: utf-8 -*-
a=float(input('digite a: '))
b=float(input('digite b: '))
c=float(input('digite c: '))
d=float(input('digite d: '))

if (a>b) and (b>c) and (c>d):
    print(a)
if (b>a) and (a>c) and (c>d):
    print(b)
if (c>a) and (a>b) and (b>d):
    print(c)
if (d>a) and (a>b) and (b>c):
    print(d)
    
if (a<b) and (b<c) and (c<d):
    print(a)
if (b<a) and (a<c) and (c<d):
    print(b)
if (c<a) and (a<b) and (b<d):
    print(c)
if (d<a) and (a<b) and (b<c):
    print(d)