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
if b>a and b>c and b>d:
    print('%d'%b)
    if a<c and a<d:
        print('%d'%a)
    if c<a and c<d:
        print('%d'%c)
    if d<a and d<c:
        print('%d'%d)
if c>a and c>b and c>d:
    print('%d'%c)
    if a<b and a<d:
        print('%d'%a)
    if b<a and b<d:  
        print('%d'%b)
    if d<a and d<b:
        print('%d'%d)
if d>a and d>b and d>c:       
    print('%d'%d)
    if a<b and a<c:
        print('%d'%a)
    if b<a and b<c:
        print('%d'%b)
    if c<a and c<b:
        print('%d'%c)