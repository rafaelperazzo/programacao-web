# -*- coding: utf-8 -*-
from __future__ import division
import math

a = int(input('Digite o valor de a:'))
b = int(input('Digite o valor de b:'))

if a>b:
    i=a
elif b>a:
    i=b
while i>0:
    if a%i==0 and b%i==0:
        print ('%d' %i)
        break
    i= i - 1
    
