# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input("Digite o valor de n:")
i=1
j=1
s=0
while i<=n:
    if i%2!=0:
        s=s+1/j
    else:
        s=s-1/j
        
    i=i+1
    j=i**2
    
print("%.5f"%s)
