# -*- coding: utf-8 -*-
from __future__ import division

p=int(input('digite p:'))
q=int(input('digite q:'))
h=0
e=q
while(e>=1):
    e=e//10
    h=h+1
f=0
while(p>0):
    if(p%(10**h)==q):
        f=f+1
        break
    p=p//5
if(f>0):
    print ('S')
else:
    print ('N')