# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input ('insira o valor de a:')
b = input ('insira o valor de b:') 

for i in range (1,b+1,1):
    if a%i==0 and b%i==0:
        c=i
print (c)
