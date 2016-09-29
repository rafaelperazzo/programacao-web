# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Digite o número 1: ')
b = input('Digite o número 2: ')
c = input('Digite o número 3: ')
d = input('Digite o número 4: ')
e = input('Digite o número 5: ')

#2
if a<b and a<c and a<d and a<e and e>b and e>c and e>d:
    print(a) 
    print(e)
elif b<a and b<c and b<d and b<e and e>a and e>c and e>d :
    print(b) 
    print(e)
elif c<a and c<b and c<d and c<e and e>a and e>b and e>d:
    print(c) 
    print(e)
elif d<a and d<b and d<c and d<e and e>a and e>b and e>c:
    print(d) 
    print(e)
elif a<b and a<c and a<e and a<d and d>b and d>c and d>e:
    print(a) 
    print(d)
elif b<a and b<c and b<e and b<d and d>a and d>c and d>e:
    print(b) 
    print(d)
elif c<a and c<b and c<e and c<d and d>a and d>b and d>e:
    print(c) 
    print(d)
elif e<a and e<b and e<c and e<d and e>a and e>b and e>c:
    print(e) 
    print(d)
elif a<b and a<d and a<e and a<c and c>b and c>d and c>e:
    print(a) 
    print(c)
elif b<a and b<d and b<e and b<c and c>a and c>d and c>e:
    print(b) 
    print(c)
elif d<a and d<b and d<e and d<c and c>a and c>b and c>e:
    print(d) 
    print(c)
elif e<a and e<b and e<d and e<c and c>a and c>b and c>d:
    print(e) 
    print(c)
elif a<c and a<d and a<e and a<b and b>c and b>d and b>e:
    print(a) 
    print(b)
elif c<a and c<d and c<e and c<b and b>a and b>d and b>e:
    print(c) 
    print(b)
elif d<a and d<c and d<e and d<b and b>a and b>c and b>e:
    print(d) 
    print(b)
elif e<a and e<c and e<d and e<b and b>a and b>c and b>c:
    print(e) 
    print(b)
elif b<c and b<d and b<e and b<a and a>c and a>d and a>e:
    print(b) 
    print(a)
elif c<b and c<d and c<e and c<a and a>b and a>d and a>e:
    print(c) 
    print(a)
elif d<b and d<c and d<e and d<a and a>b and a>c and a>e:
    print(d) 
    print(a)
elif e<b and e<c and e<d and e<a and a>b and a>c and a>d:
    print(e) 
    print(a)
elif a==b==c==d==e:
    print (a)
    print (e)