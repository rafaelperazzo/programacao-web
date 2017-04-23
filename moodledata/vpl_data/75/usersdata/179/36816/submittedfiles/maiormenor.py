# -*- coding: utf-8 -*-
import math

a = int(input('Digite o número 1: '))
b = int(input('Digite o número 2: '))
c = int(input('Digite o número 3: '))
d = int(input('Digite o número 4: '))
e = int(input('Digite o número 5: '))

if a>b and b<c and c<d and d<e:
    print('a maior')
else:
    print('a menor')
if b>a and a<c and c<d and d<e:
    print('b maior')
else:
    print('b menor')
if c>a and a<b and b<d and d<e:
    print('c maior')
else:
    print('c menor')
if d>a and a<b and b<c and c<e:
    print('d maior')
else:
    print('d menor')
if e>a and a<b and b<c and c<d:
    print('e maior')
else:
    print('e menor')    