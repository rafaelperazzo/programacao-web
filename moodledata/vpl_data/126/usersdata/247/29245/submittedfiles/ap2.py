# -*- coding: utf-8 -*-
a=float(input(''))
b=float(input(''))
c=float(input(''))
d=float(input(''))
if a>b>c>d and a>c>b>d:
    print('%d'%a)
    print('%d'%d)
elif a>c>d>b and a>d>c>b:
    print('%d'%a)
    print('%d'%b)
elif a>d>b>c and a>b>d>c:
    print('%d'%a)
    print('%d'%c)
elif d>b>c>a and d>c>b>a:
    print('%d'%d)
    print('%d'%a)
elif d>a>c>b and d>c>a>b:
    print('%d'%d)
    print('%d'%b)
elif d>b>a>c and d>a>b>c:
    print('%d'%d)
    print('%d'%c)
elif b>a>c>d and b>c>a>d:
    print('%d'%b)
    print('%d'%d)
elif b>d>c>a and b>c>d>a:
    print('%d'%b)
    print('%d'%a)
elif b>d>a>c and b>a>d>c:
    print('%d'%b)
    print('%d'%c)
elif c>b>a>d and c>a>b>d:
    print('%d'%c)
    print('%d'%d)
elif c>b>d>a and c>d>b>a:
    print('%d'%c)
    print('%d'%a)
elif c>d>a>b and c>a>d>b:
    print('%d'%c)
    print('%d'%b)