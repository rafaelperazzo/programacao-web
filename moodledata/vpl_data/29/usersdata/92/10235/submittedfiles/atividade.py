# -*- coding: utf-8 -*-
from __future__ import division
import math

n= int(input('n: '))
cont=0

while n>=1:
    n= n/10
    cont= cont+1
    
print(cont)