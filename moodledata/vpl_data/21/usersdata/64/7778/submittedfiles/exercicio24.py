# -*- coding: utf-8 -*-
from __future__ import division
import math

n1 = int(input('Digite o número 1: '))
n2 = int(input('Digite o numero 2: '))

i = 1

while (n1/i)%2==0 and (n2/i)%2==0:
    
    i = i + 1
    
    print (i)    

