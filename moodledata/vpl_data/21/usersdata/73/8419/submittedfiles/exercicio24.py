# -*- coding: utf-8 -*-
from __future__ import division
import math

a=input ('digite o valor de a:')
b=input ('digite o valor de b:')
if a>=b:
    i = a
else:
    i = b
while true:
    if a%i==0 and b%i==0:
        print (i)
        break
    i=i-1