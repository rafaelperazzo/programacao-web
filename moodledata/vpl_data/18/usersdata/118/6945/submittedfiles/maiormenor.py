# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Digite o número 1: ')
b = input('Digite o número 2: ')
c = input('Digite o número 3: ')
d = input('Digite o número 4: ')
e = input('Digite o número 5: ')

#2
if a<b<c<d<e:
    print(a) 
    print(e)
elif b<a<c<d<e :
    print(b) 
    print(e)
elif c<a<b<d<e:
    print(c) 
    print(e)
elif d<a<b<c<e:
    print(d) 
    print(e)
elif a<b<c<e<d:
    print(a) 
    print(d)
elif b<a<c<e<d:
    print(b) 
    print(d)
elif c<a<b<e<d:
    print(c) 
    print(d)
elif e<a<b<c<d:
    print(e) 
    print(d)
elif a<b<d<e<c:
    print(a) 
    print(c)
elif b<a<d<e<c:
    print(b) 
    print(c)
elif d<a<b<e<c:
    print(d) 
    print(c)
elif e<a<b<d<c:
    print(e) 
    print(c)
elif a<c<d<e<b:
    print(a) 
    print(b)
elif c<a<d<e<b:
    print(c) 
    print(b)
elif d<a<c<e<b:
    print(d) 
    print(b)
elif e<a<c<d<b:
    print(e) 
    print(b)
elif b<c<d<e<a:
    print(b) 
    print(a)
elif c<b<d<e<a:
    print(c) 
    print(a)
elif d<b<c<e<a:
    print(d) 
    print(a)
elif e<b<c<d<a:
    print(e) 
    print(a)

  
