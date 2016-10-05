# -*- coding: utf-8 -*-
from __future__ import division
import math

n1 = int(input('Digite o número 1: '))
n2 = int(input('Digite o numero 2: '))

i = n1

while (n1/i)%n1 !=0 and (n2/i)%n2 !=0:
    
    i = i - 1
    
    print str(i)

