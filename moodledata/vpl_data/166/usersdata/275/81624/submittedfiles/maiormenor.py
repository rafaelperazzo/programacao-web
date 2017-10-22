# -*- coding: utf-8 -*-
import math

a = int(input('Digite o número 1: '))
b = int(input('Digite o número 2: '))
c = int(input('Digite o número 3: '))
d = int(input('Digite o número 4: '))
e = int(input('Digite o número 5: '))

if a > b:
    if a> c:
        if a> d:
            if a> e:
                print(a)
elif b > a:
    if b> c:
        if b>d:
            if b>e:
                print (b)
elif c > a:
    if c> b:
        if c>d:
            if c>e:
                print(c)
elif d> a:
    if d > b:
        if d> c:
            if d> e:
                print(d)
elif e > a:
    if e>  b:
        if e > c:
            if e> d:
                print(e)
if a < b and c and d and e:
    print(a)
elif b < a and c and d and e:
    print (b)
elif c < a and b and d and e:
    print(c)
elif d< a and b and c and e:
    print(d)
elif e < a and b and c and d:
    print(e)