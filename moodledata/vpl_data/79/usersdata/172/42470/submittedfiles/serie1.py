# -*- coding: utf-8 -*-
import math
n=int(input('n'))
i=1
c=1
den=1
soma=1/den
while i<=n:
    if i%2==0:
        soma=soma-1/(den+1)
        i=i+1
        
            
