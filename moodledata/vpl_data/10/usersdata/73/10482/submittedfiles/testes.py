# -*- coding: utf-8 -*-
from __future__ import division
n=input ('digite n:')
for a in range (3,n+1,1):
    cont=0
    for i range (2,a,1):
        if a%i==0:
            cont=cont+1
    if cont==0:
        print a
    
    