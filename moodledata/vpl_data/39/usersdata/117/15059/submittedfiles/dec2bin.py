# -*- coding: utf-8 -*-
from __future__ import division

n=input('digite n:')

i=0
while n!=0:
    a=n%2
    a=a+i
    n=n//2
    i=i*10
    
print a