# -*- coding: utf-8 -*-
from __future__ import division
p=input('digite o valor de p:')
q=input('digite o valor de q:')
c=0
i=1
while(p//i!=0):
    c=c+1
    i=i*10
x=10**c    
c2=0
while(q>0):
    if q%x==p:
        c2=c2+1
    q=q//10
if c2>0:
    print('S')
else:
    print('N')