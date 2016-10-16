# -*- coding: utf-8 -*-
from __future__ import division
c=0
i=1
a=input('digite um numero:')
while(i<=a):
    if a%i==0:
        c=c+1
    i=i+1
if c==2:
    print('s')
else:
    print('n')
