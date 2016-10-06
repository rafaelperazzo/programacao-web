# -*- coding: utf-8 -*-
from __future__ import division
import math
n1 = int(input('Digite o número 1: '))
n2 = int(input('Digite o numero 2: '))

i = n1

while n1%i != 0 or n2 % i != 0:
    
    i = i - 1
    
print (i)
