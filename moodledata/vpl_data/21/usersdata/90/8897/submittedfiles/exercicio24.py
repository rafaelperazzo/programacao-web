# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('Digite o valor de a:'))
b=int(input('Digite o valor de b:'))

i=1
mdc=1

while i<=a and i<=b:
    if (a%i==0 and b%i==0):
        mdc=1
    i=i+1
    
print (mdc)