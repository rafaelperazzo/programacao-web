# -*- coding: utf-8 -*-
a=int(input('Digite o valor de a:'))
b=int(input('Digite o valor de b:'))
c=int(input('Digite o valor de c:'))
if a<b and a<c:
    print('%d'%a)
    if b>c:
        print('%d'%c)
        print('%d'%b)
    if c>b:
        print('%d' %b)
        print('%d'%c)
if b<a and b<c:
    print('%d'%b)
    if a>c:
        print('%d'%c)
        print('%d'%a)
    if c>a:
        print('%d' %a)
        print('%d'%c)
if c<a and c<b:
    print('%d'%c)
    if a>b:
        print('%d'%b)
        print('%d'%a)
    if b>a:
        print('%d'%a)
        print('%d'%b)
    