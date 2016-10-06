# -*- coding: utf-8 -*-
from __future__ import division
import math

x=input('Digite x: ')
y=input('Digite y: ')

i=1
mdc=1

while (i<=x and i<=y):
    
    if (x%i==0 and y%i==0):
        mdc=i
    
    i=i+1
    
print(mdc)

