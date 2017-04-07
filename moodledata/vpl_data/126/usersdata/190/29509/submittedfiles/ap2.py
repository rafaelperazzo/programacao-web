# -*- coding: utf-8 -*-
a=int(input('numero a:'))
b=int(input('numero b:'))
c=int(input('numero c:'))
d=int(input('numero d:'))
if a>=b and a>=c and a>=d:
    print(a)
    if b<=a and b<=c and b<=d:
        print(b)
    elif c<=a and c<=b and c<=d:
        print(c)
    else:
        print(d)
if b>=a and b>=c and b>=d:
    print(b)
    if a<=b and a<=c and a<=d:
        print(a)
    elif c<=a and c<=b and c<=d:
        print(c)
    else:
        print(d)
if c>=a and c>=b and c>=d:
    print(c)
    if a<=b and a<=c and a<=d:
        print(a)
    elif b<=a and b<=c and b<=d:
        print(b)
    else:
        print(d)
if d>=a and d>=b and d>=c:
    print(d)
    if a<=b and a<=c and a<=d:
        print(a)
    elif b<=a and b<=c and b<=d:
        print(b)
    else:
        print(c)