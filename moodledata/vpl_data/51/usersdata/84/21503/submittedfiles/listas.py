# -*- coding: utf-8 -*-
from __future__ import division
import math

def md(a):
    maior=0
    for i in range(0,len(a)-1,1):
        degrau=math.fabs(a[i]-a[i+1])
        if degrau>maior:
            maior=degrau
        
    return maior
        
n=input('digite quantos termos:')

while n<2:
    n=input('digite quantos termos:')
    
a=[]
for i in range(0,n,1):
    a.append(input('digite os termos da lista:'))
    
print md(a)