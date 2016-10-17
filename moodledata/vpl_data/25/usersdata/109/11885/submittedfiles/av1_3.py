# -*- coding: utf-8 -*-
from __future__ import division
import math

a=input('Digite a:')
b=input('Digite b:')
i=2
x=0


while i<=(a*b):
    if (i%a==0) and (i%b==0):
        a=i
        x=x+1
    i=i+1   
    
print (a) 
print (x)
    