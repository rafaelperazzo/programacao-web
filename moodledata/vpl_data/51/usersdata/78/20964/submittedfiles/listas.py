# -*- coding: utf-8 -*-
from __future__ import division
import math

def degrau(a):
    
    maior=0
    for i in range(o,len(a)-1,1):
        degrau=math.fabs(a[i]-a[i+1])
        if degrau>maior:
            degrau=maior
    
        return maior
a=[]
n=input('digite a quantidade de n:')
for i in range(0,n,1):
    a.append(input('digite o valor de a:'))
    
print (a)

