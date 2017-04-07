# -*- coding: utf-8 -*-
a=float(input(''))
b=float(input(''))
c=float(input(''))
d=float(input(''))
if a>b>c>d:
    print('%d'%a)
    print('%d'%d)
if a>c>d>b:
    print('%d'%a)
    print('%d'%b)
if a>d>b>c:
    print('%d'%a)
    print('%d'%c)
if d>b>c>a:
    print('%d'%d)
    print('%d'%a)
if d>a>c>b:
    print('%d'%d)
    print('%d'%b)
if d>b>a>c:
    print('%d'%d)
    print('%d'%c)
if b>a>c>d:
    print('%d'%b)
    print('%d'%d)
if b>d>c>a:
    print('%d'%b)
    print('%d'%a)
if b>b>a>c:
    print('%d'%b)
    print('%d'%c)
if c>b>a>d:
    print('%d'%c)
    print('%d'%d)
if c>b>d>a:
    print('%d'%c)
    print('%d'%a)
if c>d>a>b:
    print('%d'%c)
    print('%d'%b)