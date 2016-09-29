# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Digite o número 1: ')
b = input('Digite o número 2: ')
c = input('Digite o número 3: ')
d = input('Digite o número 4: ')
e = input('Digite o número 5: ')
if a>b and a>c and a>d and a>e:
    maior=('a')
if b>a and b>c and b>d and b>e:
    maior=('b')
if c>a and c>b and c>d and c>e:
    maior=('c')
if d>a and d>b and d>c and d>e:
    maior=('d')
if e>a and e>b and e>c and e>d:
    maior=('e')
if a<b and a<c and a<d and a<e:
    menor=('a')
if b<a and b<c and b<d and b<e:
    menor=('b')
if c<a and c<b and c<d and c<e:
    menor=('c')
if d<a and d<b and d<c and d<e:
    menor('d')
if e<a and e<b and e<c and e<d:
    menor('e')
print(maior)
print(menor)
    
    