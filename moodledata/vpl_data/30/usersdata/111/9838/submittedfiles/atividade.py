# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Número de termos: ')

i=n
x=1
s=0
while(i>=1):
    y=x/i
    s=s+y
    i=i-1
    x=x+1            
print s