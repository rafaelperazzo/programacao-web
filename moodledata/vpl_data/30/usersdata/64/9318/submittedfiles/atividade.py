# -*- coding: utf-8 -*-
from __future__ import division
import math

n = int(input('Digite o valor de n: '))


s = 0
a = 1

while n>1:
   
    s = s + a/n
        
    a = a+1
    
    
        
print ("%.5f" % s)
    
    