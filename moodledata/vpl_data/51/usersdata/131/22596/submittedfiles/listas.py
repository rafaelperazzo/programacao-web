# -*- coding: utf-8 -*-
from __future__ import division

import math
    
def degrau(a):
    degraur=0
    for i in range (0,len(a)-1,1):
    
        if math.fabs(a[i]-a[i+1])>degraur:
            degraur=math.fabs (a[i]-a[i+1])
        
            
    return degraur        


n= input('digite os numero de elementos')
a=[]
for i in range(0,n,1):
    a.append(input('digite os elementos de a:')
     
    
print ('%d' %degrau(a))    
    
    
