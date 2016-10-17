# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite n:')
soma=0
j=1
for i in range (0,n+1,1):
    if i%2==0:
        soma=soma+(1/(j*(3**i)))
    else:
        soma=soma-(1/(j*(3**i)))
    j=j+2
    i=i+1
soma= 12**(1/2)*soma
print ('%.6f' %soma)
    
