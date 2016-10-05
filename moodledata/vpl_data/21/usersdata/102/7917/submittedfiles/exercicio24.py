# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))

if a<b:
    i=a
if b<a:
    i=b
    contador=0
    
while contador==0 and i<=a and i<=b:
    if a%i==b%i==0:
        contador=contador+1
    else:
        i=i+1
print(i)
