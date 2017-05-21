# -*- coding: utf-8 -*-
import math

n=int(input('Digite n:'))
soma=0
for i in range (1,n+1,1):
    if i%2==1:
        soma=soma+(1/n)
    else:
        soma=soma-(1/n)
        
print('%.5f'%soma)
