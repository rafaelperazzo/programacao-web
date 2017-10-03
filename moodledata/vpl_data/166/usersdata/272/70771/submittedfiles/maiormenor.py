# -*- coding: utf-8 -*-
import math

a = int(input('Digite o número 1: '))
b = int(input('Digite o número 2: '))
c = int(input('Digite o número 3: '))
d = int(input('Digite o número 4: '))
e = int(input('Digite o número 5: '))

#CONTINUE...

if (a<b<c<d<e):
    print(a)

elif (b<a<c<d<e):
    print(b)

elif (c<b<a<d<e):
    print(c)

elif (d<c<b<a<e):
    print(d)

elif (e<d<c<b<a):
    print(e)

if (a>b>c>d>e):
    print(a)

elif (b>a>c>d>e):
    print(b)

elif (c>b>a>d>e):
    print(c)

elif (d>c>b>a>e):
    print(d)

elif (e>d>c>b>a):
    print(e)


