# -*- coding: utf-8 -*-
from __future__ import division
import math

a= int(input('Digite o valor do primeiro número:'))
b= int(input('Digite o valor do segundo número:'))

i=1
mdc=1

while (i<=a and i<=b):
    if (a%i==0 and b%i==0):
        mdc=i
    i=i+1

print (mdc)     
    


