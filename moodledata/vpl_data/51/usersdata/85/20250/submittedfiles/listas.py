# -*- coding: utf-8 -*-
from __future__ import division
import math

def degrau(a):
    dm=0
    for i in range(0,len(a)-1,1):
        d= math.fabs(a[i]-a[i+1])
        if d>dm:
            dm=d
    return dm
    
n= int(input('Digite o valor de n: '))
a=[]

for j in range(0,n,1):
    a.append(input('Digite os termos de a: '))
    
v= degrau(a)

print('%.d'%v)