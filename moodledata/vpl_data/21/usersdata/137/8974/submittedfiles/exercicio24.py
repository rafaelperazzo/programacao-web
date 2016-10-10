# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('a:')
b=input('b:')
while (a==0 or b==0):
    print('a ou b não pode ser divisor de zero')
    a=input('a:')
    b=input('b:')
    
r=int(a%b)
while r!=0:
    a=b
    b=r
    r=a%b
print (b)
