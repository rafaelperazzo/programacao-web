# -*- coding: utf-8 -*-
from __future__ import division
import math

def maiorDegrau(a):
    for i in range (0,len(a)-1,1):
        degrau = math.fabs(a[i]-a[i+1]) 
        if degrau>maiorDegrau:
            maior=maiorDegrau
            
    return b
    
a=[]
n = input ('Digite o valor de n:')
for i in range (0,n,1):
    for j in range (0,n,1):
        a[i,j] = input('Digite um elemento:')
        
if maiorDegrau(a):
    print ('S')
else:
    print ('N')

