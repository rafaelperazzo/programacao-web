# -*- coding: utf-8 -*-
a=int(input('Digite a:'))
b=int(input('Digite b:'))
c=int(input('Digite c:'))
d=int(input('Digite d:'))
if a>=b and a>=c and a>=d:
    print(a)
    if b<=c and b<=d:
        print(b)
    elif c<=b and c<=d:
        print(c)
    elif d<=b and d<=c:
        print(d)
if b>=a and b>=c and b>=d:
    print(b)
    if a<=c and a<=d:
        print(a)
    elif c<=a and c<=d:
        print(c)
    elif d<=a and d<=c:
        print(d)        
if c>=b and c>=a and c>=d:
    print(c)
    if b<=a and b<=d:
        print(b)
    elif a<=b and a<=d:
        print(a)
    elif d<=b and d<=a:
        print(d)      
if d>=b and d>=c and d>=a:
    print(d)
    if b<=c and b<=a:
        print(b)
    elif c<=b and c<=a:
        print(c)
    elif a<=b and a<=c:
        print(a)