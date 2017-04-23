# -*- coding: utf-8 -*-
import math

a = int(input('Digite o número 1: '))
b = int(input('Digite o número 2: '))
c = int(input('Digite o número 3: '))
d = int(input('Digite o número 4: '))
e = int(input('Digite o número 5: '))
if a<=b and a<=c and a<=d:
    print(a)
    if b>=c and b>=d:
        print(b)
    elif c>=b and c>=d:
        print(c)
    elif d>=b and d>=c:
        print(d)
elif b<=a and b<=c and b<=d:
    print(b)
    if a>=c and a>=d:
        print(a)
    elif c>=a and c>=d:
        print(c)
    elif d>=a and d>=c:
        print(d)
elif c<=a and c<=b and c<=d:
    print(c)
    if a>=b and a>=d:
        print(a)
    elif b>=a and b>=d:
        print(b)
    elif d>=a and d>=b:
        print(d)
elif d<=a and d<=b and d<=c:
    print(d)
    if a>=b and a>=c:
        print(a)
    elif b>=a and b>=c:
        print(b)
    elif c>=a and c>=b:
        print(c)
    