# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Digite o valor de a:')
b = input('Digite o valor de b:')

i=1

while (i>0):
    if a%i==0 and b%i==0:
        mdc = i
    else:
        print ('mdc = %d' %mdc)
    i = i + 1
    
