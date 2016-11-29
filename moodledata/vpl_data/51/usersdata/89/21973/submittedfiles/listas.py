# -*- coding: utf-8 -*-
from __future__ import division
import math

def modulo(x):
    if x>0:
        x=x*1
    else:
        x=x*(-1)
    
    return x
    
def maiorDegrau(a):
    maior=0
    for i in range(0,len(a)-1,1):
        degrau=math.fabs(a[i]-a[i+1])
        if degrau>maior:
            maior=degrau
            
    return maior
    
    
a=[]
for i in range(0,n,1):
    a.append(input('digite um elemento da lista a:'))
    
print(maior)