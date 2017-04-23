# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('digite o valor:'))
b=a//20
c=(a%20)
d=(a%20)//10
e=(a%20)%10
f=(a%20)%10//5
g=(a%20)%10%5
h=(a%20)%10%5//2
i=(a%20)%10%5%2
j=(a%20)%10%5%2//1
if c==0 or c!=0:
    print (b)
elif e==0 or e!=0:
    print (d)
elif g==0 or g!=0:
    print (f)
elif i==0 or i!=0:
    print (h)
else:
    print (j)

