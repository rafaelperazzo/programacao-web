# -*- coding: utf-8 -*-
from __future__ import division
import math

#ENTRADA
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')

#PROCESSAMENTO

for i in range (1,(a*b),1):
    if a%i==b%i==0 and i>1:
        print i
        elif a%i==b%i==0 and i<=1:
            print 1
    
    
    
    
    
    
    
    
    
    
    
    