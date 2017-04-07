# -*- coding: utf-8 -*-
a=float(input(''))
b=float(input(''))
c=float(input(''))
d=float(input(''))
if a>b>c>d:
    print('%d'%a)
    print('%d'%d)
elif a>c>d>b:
    print('%d'%a)
    print('%d'%b)
elif a>d>b>c:
    print('%d'%a)
    print('%d'%c)
elif d>b>c>a:
    print('%d'%d)
    print('%d'%a)
elif d>c>a>b:
    print('%d'%d)
    print('%d'%b)
elif d>b>a>c:
    print('%d'%d)
    print('%d'%c)
elif b>a>c>d:
    print('%d'%b)
    print('%d'%d)
elif b>d>c>a:
    print('%d'%b)
    print('%d'%a)
elif b>d>a>c:
    print('%d'%b)
    print('%d'%c)
elif c>b>a>d:
    print('%d'%c)
    print('%d'%d)
elif c>b>d>a:
    print('%d'%c)
    print('%d'%a)
elif c>d>a>b:
    print('%d'%c)
    print('%d'%b)