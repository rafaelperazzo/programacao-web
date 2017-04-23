# -*- coding: utf-8 -*-
import math

a = int(input('Digite o número 1: '))
b = int(input('Digite o número 2: '))
c = int(input('Digite o número 3: '))
d = int(input('Digite o número 4: '))
e = int(input('Digite o número 5: '))

if a>b and a>c and a>d and a>e:
    print(a)
if b>a and b>c and a>d and b>e:
    print(b)
if c>b and c>a and c>d and c>e:
    print(c)
if d>b and d>c and d>a and d>e:
    print(d)
if e>b and e>c and e>d and e>a:
    print(e)

