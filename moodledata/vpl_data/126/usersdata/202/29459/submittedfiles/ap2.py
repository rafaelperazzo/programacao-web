# -*- coding: utf-8 -*-
a=int(input('digite a:'))
b=int(input('digite b:'))
c=int(input('digite c:'))
d=int(input('digite d:'))
if a>b and a>c and a>d:
    print('%d'%a)
    if b<c and b<d:
        print('%d'%b)
    elif c<b and c<d:
        print('%d'%c)
    elif d<b and d<c:
        print('%d'%d)
if b>a and b>c and b>d:
    print('%d'%b)
    if a<c and a<d:
        print('%d'%a)
    elif c<a and a<d:
        print('%d'%c)
    elif d<a and d<c:
        print('%d'%d)
if c>a and c>b and c>d:
    print('%d'%c)
    if a<b and a<c:
        print('%d'%a)
    elif b<a and b<c:
        print('%d'%b)
    elif c<a and c<b:
        print('%d'%c)
if d>a and d>b and d>c:
    print('%d'%d)
    if a<b and a<c:
        print('%d'%a)
    elif b<a and b<c:
        print('%d'%b)
    elif c<a and c<b:
        print('%d'%c)
     