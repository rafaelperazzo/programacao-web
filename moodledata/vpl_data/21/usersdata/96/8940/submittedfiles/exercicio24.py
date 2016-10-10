# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('Digite a:')
b=input('Digite b:')
while(a==0or b==0):
    print('a ou b não podem ser zero')
    a=input('Digite a:')
    b=input('Digite b:')
r=int(a%b)
while r!=0:
    a=b
    b=r
    r=a%b
print(b)