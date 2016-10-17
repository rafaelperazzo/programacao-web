# -*- coding: utf-8 -*-
from __future__ import division
n=input ('digite n:')
m=input ('digite m:')
i=1
while i<=(n*m):
    if n%i==0 and m%i==0:
        print i
        break
    i=i+1
    
    