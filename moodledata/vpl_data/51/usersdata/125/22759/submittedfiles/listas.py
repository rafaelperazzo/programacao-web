# -*- coding: utf-8 -*-
from __future__ import division
def maiorDegrau(a):
    maior=0
    for i in range(0,len(a)-1,1):
        degrau=math.fabs(a[i]-a[i+1])
        if degrau>maior:
            maior=degrau
        
    return maior
    
