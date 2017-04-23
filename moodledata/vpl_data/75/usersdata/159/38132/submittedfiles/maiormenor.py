# -*- coding: utf-8 -*-
import math

a = int(input('Digite o número 1: '))
b = int(input('Digite o número 2: '))
c = int(input('Digite o número 3: '))
d = int(input('Digite o número 4: '))
e = int(input('Digite o número 5: '))

if a>=b and a>=c and a>=d and a>=e:
    print(a)
    if b<=c and b<=d and b<=e:
        print(b)
    elif c<=b and c<=d and c<=e:
        print(c)
    elif d<=b and d<=c and d<=e:
        print(d)
    elif e<=c and e<=d and e<=b:    
        print(e)
elif b>=a and b>=c and b>=d and b>=e:
    print(b)
    if a<=c and a<=d and a<=e:
        print(a)
    elif c<=a and c<=d and c<=e:
        print(c)
    elif d<=a and d<=c and d<=e:
        print(d)
    elif e<=c and e<=d and e<=a:    
        print(e)        
elif c>=b and c>=a and c>=d and c>=e:
    print(c)
    if b<=a and b<=d and b<=e:
        print(b)
    elif a<=b and c<=d and c<=e:
        print(a)
    elif d<=b and d<=a and d<=e:
        print(d)
    elif e<=a and e<=d and e<=b:    
        print(e)        
if d>=b and d>=c and d>=a and a>=e:
    print(d)
    if b<=c and b<=a and b<=e:
        print(b)
    elif c<=b and c<=a and c<=e:
        print(c)
    elif a<=b and a<=c and a<=e:
        print(a)
    elif e<=c and e<=d and e<=b:    
        print(e)        
elif e>=b and e>=c and e>=d and e>=a:
    print(e)
    if b<=c and b<=d and b<=a:
        print(b)
    elif c<=b and c<=d and c<=a:
        print(c)
    elif d<=b and d<=c and d<=a:
        print(d)
    elif a<=c and a<=d and a<=b:    
        print(a)        