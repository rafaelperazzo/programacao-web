# -*- coding: utf-8 -*-
import math

a = int(input('Digite o número 1: '))
b = int(input('Digite o número 2: '))
c = int(input('Digite o número 3: '))
d = int(input('Digite o número 4: '))
e = int(input('Digite o número 5: '))
if a<=b and a<=c and a<=d and a<=e:
    print(a)
    if b>c and b>d and b>e:
        print(b)
    elif c>b and c>d and c>e:
        print(c)
    elif d>b and d>c and d>e:
        print(d)
    elif e>b and e>c and e>d:
        print(e)
if b<=a and b<=c and b<=d and b<=e:
    print(b)
    if a>c and a>d and a>e:
        print(a)
    elif d>a and d>c and d>e:
        print(d)
    elif c>a and c>d and c>e:
        print(c)
    elif e>a and e>c and e>d:
        print(e) 
if c<=a and c<=b and c<=d and c<=e:
    print(c)
    if a>b and a>d and a>e:
        print(a)
    elif d>a and d>b and d>e:
        print(d)
    elif b>a and b>d and b>e:
        print(b)
    elif e>a and e>b and e>d:
        print(e)        
if d<=a and d<=c and d<=b and d<=e:
    print(d)
    if a>c and a>b and a>e:
        print(a)
    elif b>a and b>c and b>e:
        print(b)
    elif c>a and c>b and c>e:
        print(c)
    elif e>a and e>c and e>b:
        print(e)        
if e<=a and e<=c and e<=d and e<=b:
    print(e)
    if a>c and a>d and a>b:
        print(a)
    elif d>a and d>c and d>b:
        print(d)
    elif c>a and c>b and c>d:
        print(c)
    elif b>a and b>c and b>d:
        print(b)        
    
        
    
