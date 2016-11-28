# -*- coding: utf-8 -*-
from __future__ import division
import math

def maiordegrau(b):
    maior=0
    for i in range (0,len(b)-1,1):
        degrau=math.fabs(b[i]-b[i+1])
            if degrau>maior:
                maior=degrau
    return maior
    
a=[]
n=input('termos da lista:')
for i in range (0,n,1):
    b.append(input('elemento de b:'))
print maiordegrau(b)
            
    

