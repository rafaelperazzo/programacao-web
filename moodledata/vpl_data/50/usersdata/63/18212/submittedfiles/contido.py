# -*- coding: utf-8 -*-
from __future__ import division

n=input('Elementos em a:')
m=input('Elementos em b:')

a=[]
for i in range (0,n,1):
    a.append(input('digite valores de a:'))

b=[]
for i in range (0,m,1):
    b.append(input('digite valores de b:'))
    
for i in range (0,len(b),1):
    if b[i] in a:
        contador=contador+1
        
print contador