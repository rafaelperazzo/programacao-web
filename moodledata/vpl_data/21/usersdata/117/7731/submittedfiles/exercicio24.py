# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('Digite o valor de a:'))
b=int(input('Digite o valor de b:'))
contador=0
i=1

if a<b:
    if b%a=0:
        print (a)
if b<a:
    if a%b=0:
        print (b)
        
while i<a and i<b:
    if a%i==b%i==0:
        contador=contador+i
    i=i+1
print(i)