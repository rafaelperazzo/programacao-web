# -*- coding: utf-8 -*-
from __future__ import division
a=input('digite a:')
b=input('digite b:')
i=2
while i<=a*b:
    if i%a==0 and i%b==0:
        print i 
        break
    i=i+1
    
    