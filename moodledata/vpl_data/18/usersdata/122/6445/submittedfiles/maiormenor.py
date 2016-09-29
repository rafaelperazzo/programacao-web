# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Digite o número a: ')
b = input('Digite o número b: ')
c = input('Digite o número c: ')
d = input('Digite o número d: ')
e = input('Digite o número e: ')

#CONTINUE...

if a<b and a<c and a<d and a<e:
    print('a é o menor valor')
elif a>b and a>c and a>d and a>d:
    print('a é o maior valor')
else:
    if b>a and b>c and b>d and b>e:
        print('b é o maior valor')
    elif b<a and b<c and b<d and b<e:
        print('b é o menor valor')
        else:
            if c>a and c>b and c>d and c>e:
            print('c é o maior numero')
    elif c<a and c<b and c<d and c<e:
        print('c é o menor valor')
else:
    if d>a and d>b and d>c and d>e:
        print('d é o mairo valor')
    elif: d<a and d<b and d<c and d<e:
        print('d é o menor valor')
else:
    if e>a and e>b and e>c and e>d:
        print('e é o maior valor')
    elif e<a and e<b and e<c and e<d:
        print('e é o menor valor')