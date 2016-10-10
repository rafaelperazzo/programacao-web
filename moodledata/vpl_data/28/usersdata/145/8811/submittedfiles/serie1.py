# -*- coding: utf-8 -*-
from __future__ import division
import math
 
n=input('Digite o valor de n:')
S= 0
j = 1
i = 1
while i<=n:
    if i%2==0:
        S=S + 1/j
    else: 
        S=S - (1/j) 
    i = i + 1
    j = i**2
print ("%.5f"%S)
    
    

