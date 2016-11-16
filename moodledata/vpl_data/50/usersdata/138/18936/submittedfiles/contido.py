# -*- coding: utf-8 -*-
from __future__ import division

def congruencia(a,b,n,m):
    cont=0
    for i in range(0,n,1):
        for z in range(0,m,1):
            if a[i]==b[z]:
                cont=cont+1
    
    
    

