# -*- coding: utf-8 -*-
from __future__ import division
import math

n= input('Digite n:')
S=0
i=1
while i<=n:
    if(i%2)==1:
        S=S+(i/(i**2))
    if(i%2)==0:
        S=S-(i/(i**2))
    i=i+1
print('%.5f'%S)
