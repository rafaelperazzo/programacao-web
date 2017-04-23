# -*- coding: utf-8 -*-
import math

a = int(input('Digite o número 1: '))
b = int(input('Digite o número 2: '))
c = int(input('Digite o número 3: '))
d = int(input('Digite o número 4: '))
e = int(input('Digite o número 5: '))

#CONTINUE...
if a>b>c>d>e:
    print(a)
if b>a>c>d>e:
    print(b)
if c>b>a>d>e:
    print(c)
if d>b>c>a>e:
    print(d)
if e>b>c>d>a:
    print(e)
