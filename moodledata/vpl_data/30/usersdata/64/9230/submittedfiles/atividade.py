# -*- coding: utf-8 -*-
from __future__ import division
import math

n = int(input('Digite o valor de n: '))

i = 0
s = 0
a = 1

while n>1:
    if n < 0:
        n = n*(-1)
            
        s = a/n
        
        a = a+1
        
        n = a-1
        
        print ("%.5f" % s)
    
    else:

        s = a/n
        
        a = a+1
        
        n = a-1
        
    print ("%.5f" % s)