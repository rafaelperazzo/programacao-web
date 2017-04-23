# -*- coding: utf-8 -*-
import math

a = int(input('Digite o número 1: '))
b = int(input('Digite o número 2: '))
c = int(input('Digite o número 3: '))
d = int(input('Digite o número 4: '))
e = int(input('Digite o número 5: '))

if a>b and a>c and a>d and a>e and b<c and b<d and b<e:
    print (b)
    print (a)
elif a>b and a>c and a>d and a>e and c<b and c<d and c<e:
    print (c)
    print (a)
elif a>b and a>c and a>d and a>e and d<b and d<c and d<e:
    print (d)
    print (a)
elif a>b and a>c and a>d and a>e and e<b and e<c and e<d:
    print (e)
    print (a)
elif b>a and b>c and b>d and b>e and a<c and a<d and a<e:
    print (a)
    print (b)
elif b>a and b>c and b>d and b>e and c<a and c<d and c<e:
    print (c)
    print (b)
elif b>a and b>c and b>d and b>e and d<a and d<c and d<e:
    print (d)
    print (b)
elif b>a and b>c and b>d and b>e and e<a and e<c and e<d:
    print (e)
    print (b)
elif c>a and c>b and c>d and c>e and a<b and a<d and a<e:
    print (a)
    print (c)
elif c>a and c>b and c>d and c>e and b<a and b<d and b<e:
    print (b)
    print (c)
elif c>a and c>b and c>d and c>e and d<a and d<b and d<e:
    print (d)
    print (c)
elif c>a and c>b and c>d and c>e and e<a and e<b and e<d:
    print (e)
    print (c)
elif d>a and d>b and d>c and d>e and a<b and a<c and a<e:
    print (a)
    print (d)
elif d>a and d>b and d>c and d>e and b<a and b<c and b<e:
    print (b)
    print (d)
elif d>a and d>b and d>c and d>e and c<a and c<b and c<e:
    print (c)
    print (d)
elif d>a and d>b and d>c and d>e and e<a and e<b and e<c:
    print (e)
    print (d)
elif e>a and e>b and e>c and e>d and a<b and a<c and a<d:
    print (a)
    print (e)
elif e>a and e>b and e>c and e>d and b<a and b<c and b<d:
    print (b)
    print (e)
elif e>a and e>b and e>c and e>d and c<a and c<b and c<d:
    print (c)
    print (e)
elif e>a and e>b and e>c and e>d and d<a and d<b and d<c:
    print (d)
    print (e)