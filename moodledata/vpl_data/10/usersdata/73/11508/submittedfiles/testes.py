# -*- coding: utf-8 -*-
from __future__ import division
n=input ('digite n:')
m=input ('digite m:')
i=1
while i<=(n*m):
    if i%n==0 and i%m==0:
        print i
        break
    i=i+1
    
    