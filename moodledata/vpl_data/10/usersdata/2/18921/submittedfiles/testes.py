# -*- coding: utf-8 -*-
from __future__ import division

def congruencias(a,b,m,x0,n):
    x = []
    x.append(x0)
    
    for i in range(0,n,1):
        valor = ((a*x[i]+b)%m)/m
        x.append(valor)
    
    return x


        
    
    
    
        
    





    
    
    