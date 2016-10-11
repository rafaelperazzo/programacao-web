# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input('Digite o valor de n:'))

i=1
soma=0

if n<0:
    n=n*(-1)
    
while i<=n:
    soma=soma+i/(n-(i-1))
    i=i+1
print ('%.5f'%soma)
    
        
        

 
