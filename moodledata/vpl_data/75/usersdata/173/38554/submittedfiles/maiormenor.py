# -*- coding: utf-8 -*-
import math

a=int(input('Digite um número: '))
b=int(input('Digite um número: '))
c=int(input('Digite um número: '))
d=int(input('Digite um número: '))
e=int(input('Digite um número: '))
if((a<b)and(a<c)and(a<d)and(a<e)):
    print(a)
elif((b<a)and(b<c)and(b<d)and(b<e)):
    print(b)
elif((c<a)and(c<b)and(c<d)and(c<e)):
    print(c)
elif((d<a)and(d<b)and(d<c)and(d<e)):
    print(d)
else:
    print(e)
if((a>b)and(a>c)and(a>d)and(a>e)):
    print(a)
elif((b>a)and(b>c)and(b>d)and(b>e)):
    print(b)
elif((c>a)and(c>b)and(c>d)and(c>e)):
    print(c)
elif((d>a)and(d>b)and(d>c)and(d>e)):
    print(d)
else:
    print(e)