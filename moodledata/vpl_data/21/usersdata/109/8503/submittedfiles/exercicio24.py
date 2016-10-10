# -*- coding: utf-8 -*-
from __future__ import division
import math

a=input('Digite o valor de a:')
b=input('Digite o valor de b:')

 
for i in range (a+b,0,-1):
    if a%i==0 and b%i==0:
        print i
        break
    
