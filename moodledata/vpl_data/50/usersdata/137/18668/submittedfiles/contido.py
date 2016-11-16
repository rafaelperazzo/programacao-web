# -*- coding: utf-8 -*-
from __future__ import division
def contido (a,b):
    cont=0
    for i in range (0,len(a),1):
        if a[i] in b:
            cont= cont+1
        return cont
n=input('n:')
m=input('m:')
for i in range (0,n,1):
    a.append(input('a:'))
for i in range (0,n,1):
    b.append(input('b:'))
    print contido (a,b)
