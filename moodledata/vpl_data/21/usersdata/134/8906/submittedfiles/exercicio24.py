# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Digite o valor de a:')
b = input('Digite o valor de b:')

i=1
while a%i==0 and b%i==0:
    mdc = i
    
    i = i + 1
    print ('mdc = %d' %i)
        
    
