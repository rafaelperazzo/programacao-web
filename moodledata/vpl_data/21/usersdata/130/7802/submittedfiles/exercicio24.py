# -*- coding: utf-8 -*-
from __future__ import division
import math

a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
g=0
if a>=b:
    i=1
    while i<=b:
        if a%i==0 and b%i==0:
            g=i
        i=i+1
elif a<b:
    i=1
    while i<=a:
        if a%i==0 and b%i==0:
            g=i
        i=i+1    
    
print(g) 



    