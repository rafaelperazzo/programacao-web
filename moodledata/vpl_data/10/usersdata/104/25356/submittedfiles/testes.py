# -*- coding: utf-8 -*-
from __future__ import division
m=input('Digite um valor de m:')
pi=3
cont=0
z=2*m
for i in range(2,z+1,2):
    k=((i)*(i+1)*(i+2))
    if cont==0:
        pi=pi+(4/k)
        cont=1
    else:
        pi=pi-(4/k)
        cont=0

print ('%.15f'%(pi))
    

    
