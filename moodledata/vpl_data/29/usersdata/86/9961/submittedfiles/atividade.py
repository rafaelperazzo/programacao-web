# -*- coding: utf-8 -*-
from __future__ import division
import math

n = int(input('n:'))
cont = 1

while n//10!=0:
    n=n/10
    cont=cont+1
print(cont)
    
 