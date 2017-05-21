# -*- coding: utf-8 -*-
import math

n=int(input('digite n:'))
soma=0
for i in range (1,n+1,1):
    if 1%2==1:
        soma=soma+(1/i)
    else: 
        soma=soma-(1/i)
        
print ('%.5f'%soma)
