# -*- coding: utf-8 -*-
from __future__ import division

p=int(input('digite p:'))
q=int(input('digite q:'))
h=0
e=p
while(e>=1):
    e=e//10
    h=h+1

f=0
while(q>0):
    if(q%(10**h)==p):
        f=f+1
        break
    q=q//10
if(f>0):
    print ('S')
else:
    print ('N')